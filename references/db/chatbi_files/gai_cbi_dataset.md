# 数据集-gai_cbi_dataset

## 数据集-主表 t_gai_cbi_dataset

- **表名称：** 数据集-主表
- **表名：** t_gai_cbi_dataset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 数据集名称 | varchar | 50 |  | √ | ' ' | 数据集名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fsheetno | 附件解析sheet序号 | varchar | 50 |  | √ | ' ' | 附件解析sheet序号 |
| 5 | fmessage | 同步异常失败原因 | varchar | 2000 |  | √ | ' ' | 同步异常失败原因 |
| 6 | fdatafilter | 过滤规则 | text | 0 |  |  | null | 过滤规则 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 8 | fsourceid | 数据源id | varchar | 50 |  | √ | ' ' | 数据源id |
| 9 | fdbconfigid | 外部数据源 | int8 | 64 |  | √ | 0 | [数据连接 chatbi_dbconfig_base](../chatbi_files/chatbi_dbconfig_base.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 11 | fappid | 所属应用 | varchar | 50 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 12 | fstatus | 同步状态 | bpchar | 1 |  | √ | '0' | 同步状态,枚举: 0 :进行中 1 :成功 2 :失败 3 :已暂停 4 :未同步 5 :已取消 |
| 13 | fentityname | 实体名称 | varchar | 100 |  | √ | ' ' | 实体名称 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fsourcetype | 数据源类型 | bpchar | 1 |  | √ | '0' | 数据源类型,枚举: 2 :本地文件 4 :业务实体 5 :数据库 |
| 17 | fcloudid | 所属云 | varchar | 50 |  | √ | ' ' | [业务云 bos_devportal_bizcloud](../mdl_files/bos_devportal_bizcloud.md) |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 20 | fdesc | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 21 | ftablename | 数据库存储表名 | varchar | 50 |  | √ | ' ' | 数据库存储表名 |
| 22 | fpredata | 预置数据 | varchar | 50 |  | √ | '0' | 预置数据 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gai_cbi_dataset |  | fid |

---

## 数据集-多语言表 t_gai_cbi_dataset_l

- **表名称：** 数据集-多语言表
- **表名：** t_gai_cbi_dataset_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 数据集名称 | varchar | 50 |  | √ | ' ' | 数据集名称 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gai_cbi_dataset_l |  | fpkid |

---

## 字段元数据-子表 t_gai_cbi_dataset_meta

- **表名称：** 字段元数据-子表
- **表名：** t_gai_cbi_dataset_meta

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldstatus | 字段有效性 | varchar | 10 |  | √ | ' ' | 字段有效性,枚举: enable :有效 disable :失效 |
| 3 | fdisplayname | 字段名称 | varchar | 255 |  | √ | ' ' | 字段名称 |
| 4 | ffieldname | 列名 | varchar | 255 |  | √ | ' ' | 列名 |
| 5 | fdefaultmethod | 指标默认聚合方式 | varchar | 50 |  | √ | ' ' | 指标默认聚合方式,枚举: :- SUM :求和 COUNT :计算 COUNT_DISTINCT :不重复计数 MAX :最大值 MIN :最小值 AVG :平均值 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | ffieldcode | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 8 | ffieldtype | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型,枚举: TEXT :文本 NUM :数值 DATE :日期 |
| 9 | findextype | 维度/指标 | varchar | 50 |  | √ | ' ' | 维度/指标,枚举: DIMENSION :维度 METRIC :指标 |
| 10 | fdefaultvalue | 缺省值 | varchar | 50 |  | √ | ' ' | 缺省值 |
| 11 | fdisplayformatstr | 显示格式化字符串 | varchar | 255 |  | √ | ' ' | 显示格式化字符串 |
| 12 | fdisplayformat | 显示格式 | varchar | 50 |  | √ | ' ' | 显示格式 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fdefaultvaluemethod | 维度默认取值方式 | varchar | 255 |  | √ | ' ' | 维度默认取值方式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_gai_cbi_dsm_fid |  | fid |
| 2 | pk_gai_cbi_dataset_meta |  | fentryid |
