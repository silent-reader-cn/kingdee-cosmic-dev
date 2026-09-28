# 全局控制-privacy_global_control

## 全局控制-主表 t_privacy_global_control

- **表名称：** 全局控制-主表
- **表名：** t_privacy_global_control

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fdailytotallimit | 每日解密总上限 | int8 | 64 |  |  | null | 每日解密总上限 |
| 5 | fmessagechannel | 消息渠道 | varchar | 50 |  | √ | ' ' | 消息渠道,枚举: CLOUDHUB :云之家 EMAIL :邮件 MESSAGE :短信 |
| 6 | fspecialperm | 特殊权限控制 | varchar | 50 |  |  | ' ' | 特殊权限控制,枚举: CREATOR :创建人 |
| 7 | fsupportsearch | 脱敏字段支持查询 | bpchar | 1 |  | √ | '0' | 脱敏字段支持查询 |
| 8 | fcheckdesenperm | 启用脱敏权限控制 | bpchar | 1 |  |  | '0' | 启用脱敏权限控制 |
| 9 | fcontrolrule | 控制规则 | varchar | 50 |  | √ | ' ' | 控制规则,枚举: NOTALLOW :不允许超过上限 EARLYWARN :超过最大次数预警 |
| 10 | ftemplate | 消息模板 | varchar | 500 |  | √ | ' ' | 消息模板 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_privacy_global_control |  | fid |

---

## 消息接收人-多选基础资料表 t_privacy_global_receive

- **表名称：** 消息接收人-多选基础资料表
- **表名：** t_privacy_global_receive

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_privacy_global_receive |  | fpkid |
