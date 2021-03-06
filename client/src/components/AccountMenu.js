import React from 'react'
import { Menu } from 'grommet'
import { useDispatch } from 'react-redux'
import { useHistory } from 'react-router-dom'

import { signOut } from '../store/auth'

const AccountMenu = () => {
  const dispatch = useDispatch()
  let history = useHistory()

  const handleClick = () => {
    dispatch(signOut())
  }
  return (
    <Menu
      size="small"
      icon={false}
      focusIndicator={false}
      hoverIndicator={{ color: "#ffffff" }}
      label="Account"
      items={[
        { label: 'Settings', onClick: () => {history.push("/settings") } },
        { label: 'Signout', onClick: () => handleClick() },
      ]}
    />
  )
}

export default AccountMenu
