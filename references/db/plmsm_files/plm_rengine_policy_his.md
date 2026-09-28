# 策略配置操作（规则引擎）-plm_rengine_policy_his

## 策略配置操作（规则引擎）-主表 t_plm_egn_policy_his

- **表名称：** 策略配置操作（规则引擎）-主表
- **表名：** t_plm_egn_policy_his

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foperate | 操作 | varchar | 20 |  | √ | ' ' | 操作,枚举: new :新增 modify :修改 delete :删除 enable :启用 disable :禁用 |
| 3 | fname | 策略名称 | varchar | 100 |  | √ | ' ' | 策略名称 |
| 4 | foperatorid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | foperatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 6 | fnumber | 策略编码 | varchar | 50 |  | √ | ' ' | 策略编码 |
| 7 | fpolicyid | 策略id | int8 | 64 |  | √ | 0 | 策略id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_egn_policy_his |  | fid |
| 2 | idx_plm_policy_his |  | fpolicyid,fnumber |

---

## 策略配置操作（规则引擎）-多语言表 t_plm_egn_policy_his_l

- **表名称：** 策略配置操作（规则引擎）-多语言表
- **表名：** t_plm_egn_policy_his_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 策略名称 | varchar | 100 |  | √ | ' ' | 策略名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_egn_policy_his_l |  | fpkid |
| 2 | idx_plm_policy_his_l |  | fid,flocaleid |
