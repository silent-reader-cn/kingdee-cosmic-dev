# 集成日志-ccas_integratedlog

## 集成日志-多语言表 t_ccas_integratedlog_l

- **表名称：** 集成日志-多语言表
- **表名：** t_ccas_integratedlog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpkgname | 集成服务名称 | varchar | 80 |  | √ | ' ' | 集成服务名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 40 |  | √ | ' ' | pkid |
| 5 | fcreateorg | 集成服务商 | varchar | 80 |  | √ | ' ' | 集成服务商 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ccas_integratedlog_l |  | fpkid |
| 2 | idx_ccas_integratedlog_l |  | fid,flocaleid |

---

## 集成日志-主表 t_ccas_integratedlog

- **表名称：** 集成日志-主表
- **表名：** t_ccas_integratedlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcaller | 调用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fportname | 接口名称 | varchar | 80 |  | √ | ' ' | 接口名称 |
| 4 | finparameter_tag | 请求参数_详情 | text | 0 |  |  | ' ' | 请求参数_详情 |
| 5 | fresult | 返回结果 | text | 0 |  |  | ' ' | 返回结果 |
| 6 | fcallorg | 调用组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fcalldatetime | 调用时间 | timestamp | 0 |  |  | null | 调用时间 |
| 8 | fcreateorg | 集成服务商 | varchar | 80 |  | √ | ' ' | 集成服务商 |
| 9 | fresult_tag | 返回结果_详情 | text | 0 |  |  | ' ' | 返回结果_详情 |
| 10 | fbillnumber | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 11 | frequesturl | 请求URL | varchar | 2000 |  | √ | ' ' | 请求URL |
| 12 | fappname | 应用 | varchar | 80 |  | √ | ' ' | 应用 |
| 13 | fpkgname | 集成服务名称 | varchar | 80 |  | √ | ' ' | 集成服务名称 |
| 14 | fcallstatus | 调用状态 | bpchar | 1 |  | √ | '1' | 调用状态,枚举: 0 :失败 1 :成功 |
| 15 | fnumber | 日志编号 | varchar | 80 |  | √ | ' ' | 日志编号 |
| 16 | fcloud | 云 | varchar | 80 |  | √ | ' ' | 云 |
| 17 | finparameter | 请求参数 | text | 0 |  |  | ' ' | 请求参数 |
| 18 | foperation | 业务操作 | varchar | 80 |  | √ | ' ' | 业务操作 |
| 19 | fbilltype | 单据类型 | varchar | 80 |  | √ | ' ' | 单据类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ccas_integratedlog |  | fid |
| 2 | idx_ccas_integratedlog |  | fbillnumber |
