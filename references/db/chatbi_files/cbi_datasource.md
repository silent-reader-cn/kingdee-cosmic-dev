# 数据源-cbi_datasource

## 数据源-主表 t_cbi_datasource

- **表名称：** 数据源-主表
- **表名：** t_cbi_datasource

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 数据源名称 | varchar | 255 |  | √ | ' ' | 数据源名称 |
| 4 | fdatafilter | 过滤规则 | text | 0 |  |  | null | 过滤规则 |
| 5 | ftrdindexid | saas指标库指标id | varchar | 100 |  | √ | ' ' | saas指标库指标id |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 7 | fbizname | 实体名称 | varchar | 255 |  | √ | ' ' | 实体名称 |
| 8 | fdbconfigid | 外部数据源 | int8 | 64 |  | √ | 0 | [数据连接 chatbi_dbconfig_base](../chatbi_files/chatbi_dbconfig_base.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 10 | fappid | 所属应用 | varchar | 50 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 11 | fpicture | 图片logo | varchar | 255 |  | √ | ' ' | 图片logo |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fsourcetype | 数据源类型 | varchar | 50 |  | √ | ' ' | 数据源类型,枚举: 2 :本地文件 4 :业务实体 5 :数据库 6 :SaaS指标库 |
| 15 | fcloudid | 所属云 | varchar | 50 |  | √ | ' ' | [业务云 bos_devportal_bizcloud](../mdl_files/bos_devportal_bizcloud.md) |
| 16 | fbizcode | 实体编码 | varchar | 255 |  | √ | ' ' | 实体编码 |
| 17 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 19 | ftablename | 数据库表名 | varchar | 255 |  | √ | ' ' | 数据库表名 |
| 20 | ftrdmetricid | 来源指标库 | int8 | 64 |  | √ | 0 | [第三方指标 cbi_trd_metric](../chatbi_files/cbi_trd_metric.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_datasource |  | fid |

---

## -附件表 t_cbi_datasource_file

- **表名称：** -附件表
- **表名：** t_cbi_datasource_file

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_datasource_file |  | fpkid |
| 2 | idx_cbi_datasource_file |  | fid |

---

## 字段元数据-子表 t_cbi_datasource_meta

- **表名称：** 字段元数据-子表
- **表名：** t_cbi_datasource_meta

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbdformid | 所属基础资料formId | varchar | 255 |  | √ | ' ' | 所属基础资料formId |
| 3 | fdisplayname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 4 | ffieldname | 源字段名称 | varchar | 255 |  | √ | ' ' | 源字段名称 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbdfieldcode | 基础资料属性code | varchar | 255 |  | √ | ' ' | 基础资料属性code |
| 7 | fvaluesourcetype | 取值来源 | varchar | 50 |  | √ | ' ' | 取值来源,枚举: SYSTEM_TIME :系统时间 |
| 8 | ffieldcode | 源字段编码 | varchar | 255 |  | √ | ' ' | 源字段编码 |
| 9 | famountname | 合计行的值名称 | varchar | 255 |  | √ | ' ' | 合计行的值名称 |
| 10 | ffieldtype | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型,枚举: TEXT :文本 NUM :数值 DATE :日期 BASE_DATA :基础资料 |
| 11 | findextype | 维度/度量 | varchar | 50 |  | √ | ' ' | 维度/度量,枚举: DIMENSION :维度 METRIC :度量 |
| 12 | fbdname | 所属基础资料 | varchar | 255 |  | √ | ' ' | 所属基础资料 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fcode | 字段编码 | varchar | 255 |  | √ | ' ' | 字段编码 |
| 15 | fbdfield | 所属基础资料字段 | varchar | 500 |  | √ | ' ' | 所属基础资料字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_datasource_meta |  | fentryid |
| 2 | idx_cbi_datas_meta_fid |  | fid |
