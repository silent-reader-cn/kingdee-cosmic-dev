# 单据关系配置-bpm_billrelationmodel

## 单据关系配置-主表 t_bpm_relationmodel

- **表名称：** 单据关系配置-主表
- **表名：** t_bpm_relationmodel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | frelationtypeid | 关系类型 | int8 | 64 |  | √ | 0 | 单据关系类型 bpm_billrelationtype |
| 4 | frelationtype | 关系类型 | varchar | 50 |  | √ | ' ' | 关系类型,枚举: |
| 5 | ftargetbill | 目标单 | varchar | 200 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 6 | fpreinsert | 内置数据 | bpchar | 1 |  | √ | '0' | 内置数据 |
| 7 | fenable | 启用 | bpchar | 1 |  | √ | '1' | 启用 |
| 8 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 9 | fsrcbill | 源单 | varchar | 200 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 10 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 11 | fparamjson | 参数 | text | 0 |  |  | null | 参数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bpm_relationmodel_number |  | fnumber |
| 2 | idx_bpm_relationmodel_bill |  | ftargetbill,fsrcbill |
| 3 | pk_t_bpm_relationmodel |  | fid |

---

## 单据关系配置-多语言表 t_bpm_relationmodel_l

- **表名称：** 单据关系配置-多语言表
- **表名：** t_bpm_relationmodel_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bpm_relationmodel_l |  | fid,flocaleid |
| 2 | pk_t_bpm_relationmodel_l |  | fpkid |
