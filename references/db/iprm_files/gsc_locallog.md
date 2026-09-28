# 本地化日志-gsc_locallog

## 本地化日志-主表 t_gsc_locallog

- **表名称：** 本地化日志-主表
- **表名：** t_gsc_locallog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgscendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 3 | fgscresult_tag | 返回结果_详情 | text | 0 |  |  | ' ' | 返回结果_详情 |
| 4 | fgscstarttime | 调用时间 | timestamp | 0 |  |  | null | 调用时间 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | varchar | 2 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatorid | 调用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fgscbillnumber | 单据编号 | varchar | 256 |  | √ | ' ' | 单据编号 |
| 10 | fgscoperation | 业务操作 | varchar | 80 |  | √ | ' ' | 业务操作 |
| 11 | fgscrequesturl | 请求URL | varchar | 2000 |  | √ | ' ' | 请求URL |
| 12 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fgscinparameter | 请求参数 | text | 0 |  |  | ' ' | 请求参数 |
| 15 | fgsccallorg | 调用组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fgscresult | 返回结果 | text | 0 |  |  | ' ' | 返回结果 |
| 18 | fgscportname | 接口名称 | varchar | 80 |  | √ | ' ' | 接口名称 |
| 19 | fgsccountry | 国家/地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 20 | fgsctraceid | 日志TraceId | varchar | 100 |  | √ | ' ' | 日志TraceId |
| 21 | fgscinparameter_tag | 请求参数_详情 | text | 0 |  |  | ' ' | 请求参数_详情 |
| 22 | fgscbusiness | 业务对象 | varchar | 50 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |
| 23 | fgsccallstatus | 调用状态 | varchar | 2 |  | √ | ' ' | 调用状态,枚举: 0 :失败 1 :成功 |
| 24 | fenable | 使用状态 | varchar | 2 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 日志编码 | varchar | 30 |  | √ | ' ' | 日志编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gsc_locallog |  | fid |
| 2 | idx_gsc_locallog_bus |  | fgscbusiness |
| 3 | idx_gsc_locallog_country |  | fgsccountry |
| 4 | idx_gsc_locallog_num |  | fnumber |
| 5 | idx_gsc_locallog_billnum |  | fgscbillnumber |
| 6 | idx_gsc_locallog_op |  | fgscoperation |
| 7 | idx_gsc_locallog_starttime |  | fgscstarttime |
| 8 | idx_gsc_locallog_port |  | fgscportname |

---

## 本地化日志-多语言表 t_gsc_locallog_l

- **表名称：** 本地化日志-多语言表
- **表名：** t_gsc_locallog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gsc_locallog_l |  | fpkid |
| 2 | idx_gsc_locallog_l_l_fid |  | fid,flocaleid |
