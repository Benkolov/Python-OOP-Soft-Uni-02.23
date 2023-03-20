from project.team import Team

import unittest


class TestTeam(unittest.TestCase):

    def test_create_team(self):
        team = Team("TeamA")
        self.assertEqual(team.name, "TeamA")
        self.assertEqual(len(team.members), 0)

    def test_create_team_with_invalid_name(self):
        with self.assertRaises(ValueError):
            Team("Team1")

    def test_add_member(self):
        team = Team("TeamA")
        result = team.add_member(John=25, Jane=30)
        self.assertEqual(result, "Successfully added: John, Jane")
        self.assertEqual(team.members, {"John": 25, "Jane": 30})

    def test_remove_member(self):
        team = Team("TeamA")
        team.add_member(John=25, Jane=30)
        result = team.remove_member("John")
        self.assertEqual(result, "Member John removed")
        self.assertEqual(team.members, {"Jane": 30})

    def test_remove_nonexistent_member(self):
        team = Team("TeamA")
        team.add_member(John=25, Jane=30)
        result = team.remove_member("Jack")
        self.assertEqual(result, "Member with name Jack does not exist")

    def test_gt(self):
        team1 = Team("TeamA")
        team1.add_member(John=25, Jane=30)
        team2 = Team("TeamB")
        team2.add_member(Mark=35)
        self.assertTrue(team1 > team2)

    def test_len(self):
        team = Team("TeamA")
        team.add_member(John=25, Jane=30, Mark=35)
        self.assertEqual(len(team), 3)

    def test_add_teams(self):
        team1 = Team("TeamA")
        team1.add_member(John=25, Jane=30)
        team2 = Team("TeamB")
        team2.add_member(Mark=35)
        team3 = team1 + team2
        self.assertEqual(team3.name, "TeamATeamB")
        self.assertEqual(team3.members, {"John": 25, "Jane": 30, "Mark": 35})

    def test_str(self):
        team = Team("TeamA")
        team.add_member(John=25, Jane=30, Mark=35)
        expected_output = "Team name: TeamA\nMember: Mark - 35-years old\nMember: Jane - 30-years old\nMember: John - 25-years old"
        self.assertEqual(str(team), expected_output)

    def test_set_name_valid(self):
        team = Team("TeamA")
        team.name = "TeamB"
        self.assertEqual(team.name, "TeamB")

    def test_set_name_invalid(self):
        team = Team("TeamA")
        with self.assertRaises(ValueError):
            team.name = "123"

    def test_add_member_with_existing_name(self):
        team = Team("TeamA")
        team.add_member(John=25)
        result = team.add_member(John=30)
        self.assertEqual(result, "Successfully added:")
        self.assertEqual(team.members, {"John": 25})

    def test_add_multiple_members(self):
        team = Team("TeamA")
        result = team.add_member(John=25, Jane=30, Mark=35)
        self.assertEqual(result, "Successfully added: John, Jane, Mark")
        self.assertEqual(team.members, {"John": 25, "Jane": 30, "Mark": 35})

    def test_remove_multiple_members(self):
        team = Team("TeamA")
        team.add_member(John=25, Jane=30, Mark=35)
        team.remove_member("John")
        team.remove_member("Jane")
        self.assertEqual(team.members, {"Mark": 35})

    def test_gt_with_same_number_of_members(self):
        team1 = Team("TeamA")
        team1.add_member(John=25)
        team2 = Team("TeamB")
        team2.add_member(Mark=35)
        self.assertFalse(team1 > team2)

    def test_gt_with_less_members(self):
        team1 = Team("TeamA")
        team1.add_member(John=25)
        team2 = Team("TeamB")
        team2.add_member(Mark=35, Jane=30)
        self.assertFalse(team1 > team2)

    def test_len_zero_members(self):
        team = Team("TeamA")
        self.assertEqual(len(team), 0)

    def test_add_teams_with_no_members(self):
        team1 = Team("TeamA")
        team2 = Team("TeamB")
        team3 = team1 + team2
        self.assertEqual(team3.name, "TeamATeamB")
        self.assertEqual(team3.members, {})

    def test_str_with_no_members(self):
        team = Team("TeamA")
        expected_output = "Team name: TeamA"
        self.assertEqual(str(team), expected_output)




if __name__ == "__main__":
    unittest.main()
