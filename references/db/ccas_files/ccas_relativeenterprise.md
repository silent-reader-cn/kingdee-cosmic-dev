# 相对方法人企业-ccas_relativeenterprise

## 相对方法人企业-主表 t_ccas_relativeenterprise

- **表名称：** 相对方法人企业-主表
- **表名：** t_ccas_relativeenterprise

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 200 |  | √ | ' ' | 备注 |
| 3 | fexistopencorpid | 已认证ID | varchar | 255 |  | √ | ' ' | 已认证ID |
| 4 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 7 | fstatus | 数据状态 | varchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fintegrationservice | 集成服务 | int8 | 64 |  | √ | 0 | [集成服务配置 ccas_cisconfig](../ccas_files/ccas_cisconfig.md) |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fpeerserviceadmin | 相对方服务管理员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fenable | 使用状态 | varchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fauthenstatus | 企业认证状态 | varchar | 1 |  | √ | ' ' | 企业认证状态,枚举: A :待认证 B :已认证 C :认证中 |
| 13 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 14 | frelativeenterprise | 相对方法人企业 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 15 | fcompanyid | 企业ID | varchar | 255 |  | √ | ' ' | 企业ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ccas_relativeenterprise |  | fid |

---

## 相对方法人企业-多语言表 t_ccas_relativeenterprise_l

- **表名称：** 相对方法人企业-多语言表
- **表名：** t_ccas_relativeenterprise_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 10 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ccas_relativeenterprise_l |  | fpkid |
| 2 | udx_ccas_relativeenterprise_l |  | fid,flocaleid |
