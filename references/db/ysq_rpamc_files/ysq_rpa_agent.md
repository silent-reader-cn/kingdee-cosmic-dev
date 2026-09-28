# 终端管理-ysq_rpa_agent

## 终端管理-主表 tk_ysq_rpa_agent

- **表名称：** 终端管理-主表
- **表名：** tk_ysq_rpa_agent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_ysq_agent_version | 终端版本 | varchar | 32 |  | √ | ' ' | 终端版本 |
| 3 | fk_ysq_rpa_user_name | RPA系统用户名 | varchar | 254 |  | √ | ' ' | RPA系统用户名 |
| 4 | fk_ysq_rdp_port | RDP端口 | int8 | 64 |  |  | null | RDP端口 |
| 5 | fk_ysq_conn_faile_msg_tag | 连接失败原因_详情 | text | 0 |  |  | null | 连接失败原因_详情 |
| 6 | forgid | 组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 7 | fk_ysq_conn_faile_msg | 连接失败原因 | varchar | 255 |  | √ | ' ' | 连接失败原因 |
| 8 | fk_ysq_agent_no | 实例号 | varchar | 128 |  | √ | ' ' | 实例号 |
| 9 | fk_ysq_last_conn_time | 最近连接时间 | timestamp | 0 |  |  | null | 最近连接时间 |
| 10 | fk_ysq_desktop_type | 桌面类型 | varchar | 32 |  | √ | ' ' | 桌面类型 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fk_ysq_comm_token | 通信token | varchar | 64 |  | √ | ' ' | 通信token |
| 13 | fk_ysq_user_domain | 终端系统域名 | varchar | 128 |  | √ | ' ' | 终端系统域名 |
| 14 | fk_ysq_last_login_time | 上传登录时间 | timestamp | 0 |  |  | null | 上传登录时间 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 16 | fk_ysq_data_status | 运行状态 | varchar | 50 |  | √ | ' ' | 运行状态,枚举: busy :运行 free :空闲 offline :离线 |
| 17 | fk_ysq_agent_os | 终端操作系统 | varchar | 128 |  | √ | ' ' | 终端操作系统 |
| 18 | fk_ysq_description | 描述信息 | varchar | 254 |  | √ | ' ' | 描述信息 |
| 19 | fk_ysq_agent_ip | 地址 | varchar | 128 |  | √ | ' ' | 地址 |
| 20 | fk_ysq_user_name | 终端用户名 | varchar | 128 |  | √ | ' ' | 终端用户名 |
| 21 | fk_ysq_agent_type | 终端类型 | varchar | 50 |  | √ | ' ' | 终端类型,枚举: robot :无人值守机器人 studio :设计器 assistant :有人值守机器人 standardRobot :通用场景机器人 |
| 22 | fk_ysq_last_heart_time | 上次心跳时刻 | timestamp | 0 |  |  | null | 上次心跳时刻 |
| 23 | fk_ysq_agent_dcode | 机器码 | varchar | 128 |  | √ | ' ' | 机器码 |
| 24 | fk_ysq_agent_uncode | 终端唯一标识 | varchar | 128 |  | √ | ' ' | 终端唯一标识 |
| 25 | fk_ysq_access_token | 终端登录后accesstoken | varchar | 512 |  | √ | ' ' | 终端登录后accesstoken |
| 26 | fk_ysq_identity_desc | 当前身份描述 | varchar | 64 |  | √ | ' ' | 当前身份描述 |
| 27 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 28 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 29 | fk_ysq_identity_fid | 当前身份ID | int8 | 64 |  |  | null | 当前身份ID |
| 30 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 31 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 32 | fk_ysq_conn_ip | 连接用IP | varchar | 128 |  | √ | ' ' | 连接用IP |
| 33 | fk_ysq_win_status | 桌面状态 | varchar | 50 |  | √ | ' ' | 桌面状态,枚举: succ :已连接 failed :连接失败 unconn :未连接 unbind :未绑定管家 |
| 34 | fk_ysq_client_resolution | 终端分辨率 | varchar | 16 |  | √ | ' ' | 终端分辨率 |
| 35 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 36 | fk_ysq_agent_name | 机器名 | varchar | 128 |  | √ | ' ' | 机器名 |
| 37 | fk_ysq_client_pwd | 终端登录密码 | varchar | 128 |  | √ | ' ' | 终端登录密码 |
| 38 | fk_ysq_next_action | 下次动作 | varchar | 16 |  | √ | ' ' | 下次动作 |
| 39 | fk_ysq_is_manager | 是否管理者绑定 | varchar | 50 |  | √ | ' ' | 是否管理者绑定,枚举: yes :是 no :否 |
| 40 | fk_ysq_agent_alias | 别名 | varchar | 128 |  | √ | ' ' | 别名 |
| 41 | fk_ysq_status | 机器人状态 | varchar | 50 |  | √ | ' ' | 机器人状态,枚举: yes :启用 no :停用 |
| 42 | fk_ysq_under_managerment | 是否绑定桌面管家 | varchar | 50 |  | √ | ' ' | 是否绑定桌面管家,枚举: yes :是 no :否 |
| 43 | fauditorid | 审核人 | int8 | 64 |  |  | null | 人员 bos_user |
| 44 | fk_ysq_auto_login | 是否自动登录 | varchar | 50 |  | √ | ' ' | 是否自动登录,枚举: yes :是 no :否 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tk_ysq_rpa_agent |  | fid |
| 2 | idx_tk_ysq_rpa_agent_no_dcode_0 |  | fk_ysq_agent_no,fk_ysq_agent_dcode |

---

## 终端管理-多语言表 tk_ysq_rpa_agent_l

- **表名称：** 终端管理-多语言表
- **表名：** tk_ysq_rpa_agent_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_ysq_description | 描述信息 | varchar | 254 |  | √ | ' ' | 描述信息 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fk_ysq_agent_alias | 别名 | varchar | 128 |  | √ | ' ' | 别名 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | fk_ysq_identity_desc | 当前身份描述 | varchar | 64 |  | √ | ' ' | 当前身份描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tk_ysq_rpa_agent_l |  | fpkid |
| 2 | idx__ysq_rpa_agent_l_0 |  | fid,flocaleid |
