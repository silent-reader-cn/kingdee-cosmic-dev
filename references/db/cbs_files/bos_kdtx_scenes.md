# 业务场景配置-bos_kdtx_scenes

## 告警通知人员-多选基础资料表 t_cbs_dtx_alarm_user

- **表名称：** 告警通知人员-多选基础资料表
- **表名：** t_cbs_dtx_alarm_user

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_dtx_alarm_user_fk |  | fid |
| 2 | pk_cbs_dtx_alarm_user |  | fpkid |

---

## 单据体-多语言表 t_cbs_dtx_branch_scenes_l

- **表名称：** 单据体-多语言表
- **表名：** t_cbs_dtx_branch_scenes_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 分支备注 | varchar | 500 |  | √ | ' ' | 分支备注 |
| 2 | fname | 分支场景名 | varchar | 255 |  | √ | ' ' | 分支场景名 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbs_dtx_branch_scenes_l |  | fpkid |
| 2 | idx_cbs_dtx_branch_scenes_l_0 |  | fentryid,flocaleid |

---

## 单据体-子表 t_cbs_dtx_branch_scenes

- **表名称：** 单据体-子表
- **表名：** t_cbs_dtx_branch_scenes

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 分支备注 | varchar | 500 |  |  | ' ' | 分支备注 |
| 3 | fname | 分支场景名 | varchar | 255 |  | √ | ' ' | 分支场景名 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fcode | 分支场景编码 | varchar | 100 |  | √ | ' ' | 分支场景编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_dtx_branch_scenes |  | fentryid,fcode |
| 2 | pk_t_cbs_dtx_branch_scenes |  | fentryid |

---

## 业务场景配置-多语言表 t_cbs_dtx_tx_scenes_l

- **表名称：** 业务场景配置-多语言表
- **表名：** t_cbs_dtx_tx_scenes_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 3 | fname | 场景名 | varchar | 255 |  | √ | ' ' | 场景名 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_dtx_tx_scenes_l_0 |  | fid,flocaleid |
| 2 | pk_t_cbs_dtx_tx_scenes_l |  | fpkid |

---

## 业务场景配置-主表 t_cbs_dtx_tx_scenes

- **表名称：** 业务场景配置-主表
- **表名：** t_cbs_dtx_tx_scenes

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 500 |  |  | ' ' | 备注 |
| 3 | fname | 场景名 | varchar | 255 |  | √ | ' ' | 场景名 |
| 4 | fphone | fphone | varchar | 240 |  | √ | ' ' |  |
| 5 | fnotice_operator | 是否通知操作人 | bpchar | 1 |  | √ | '0' | 是否通知操作人 |
| 6 | fapp | 所属应用 | varchar | 100 |  | √ | ' ' | 所属应用 |
| 7 | falarm_type | 告警通知方式 | varchar | 200 |  | √ | ' ' | 告警通知方式,枚举: sms :短信 email :邮件 yunzhijia :云之家 |
| 8 | froutekey | froutekey | varchar | 50 |  |  | ' ' |  |
| 9 | fcode | 场景编码 | varchar | 100 |  | √ | ' ' | 场景编码 |
| 10 | fbusiness_type | 业务类型 | varchar | 100 |  |  | ' ' | 业务类型 |
| 11 | fappid | fappid | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_dtx_tx_scenes |  | fcode |
| 2 | pk_t_cbs_dtx_tx_scenes |  | fid |
