# 扩展状态表G(标准预留)-src_project_ext_g

## 扩展状态表G(标准预留)-主表 t_src_project_ext

- **表名称：** 扩展状态表G(标准预留)-主表
- **表名：** t_src_project_ext

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 3 | fsourceid | fsourceid | int8 | 64 |  | √ | 0 |  |
| 4 | ftieredtype | ftieredtype | bpchar | 1 |  | √ | '1' |  |
| 5 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 6 | fbilldate | fbilldate | timestamp | 0 |  |  | null |  |
| 7 | fpurdeptid | fpurdeptid | int8 | 64 |  | √ | 0 |  |
| 8 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 9 | fsystype | fsystype | bpchar | 1 |  | √ | '1' |  |
| 10 | fsrctypeid | fsrctypeid | int8 | 64 |  | √ | 0 |  |
| 11 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 12 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 13 | fopentype | fopentype | bpchar | 1 |  | √ | ' ' |  |
| 14 | fsceneid | fsceneid | int8 | 64 |  | √ | 0 |  |
| 15 | fpurgroupid | fpurgroupid | int8 | 64 |  | √ | 0 |  |
| 16 | ftendertype | ftendertype | bpchar | 1 |  | √ | ' ' |  |
| 17 | fbiztypeid | fbiztypeid | int8 | 64 |  | √ | 0 |  |
| 18 | fismultipackage | fismultipackage | bpchar | 1 |  | √ | '0' |  |
| 19 | fsourceclassid | fsourceclassid | int8 | 64 |  | √ | 0 |  |
| 20 | fopenstatus | fopenstatus | bpchar | 1 |  | √ | '1' |  |
| 21 | fmanagetype | fmanagetype | bpchar | 1 |  | √ | ' ' |  |
| 22 | funauditorid | funauditorid | int8 | 64 |  | √ | 0 |  |
| 23 | ftaxtype | ftaxtype | varchar | 30 |  | √ | ' ' |  |
| 24 | fbillno | fbillno | varchar | 30 |  | √ | ' ' |  |
| 25 | fbidname | fbidname | varchar | 300 |  | √ | ' ' |  |
| 26 | fterminalnode | fterminalnode | int8 | 64 |  | √ | 0 |  |
| 27 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 28 | funsubmitterid | funsubmitterid | int8 | 64 |  | √ | 0 |  |
| 29 | funsubmitdate | funsubmitdate | timestamp | 0 |  |  | null |  |
| 30 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 31 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 32 | fparentid | fparentid | varchar | 50 |  | √ | ' ' |  |
| 33 | fsubmitterid | fsubmitterid | int8 | 64 |  | √ | 0 |  |
| 34 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 35 | fsrcbillid | fsrcbillid | varchar | 50 |  | √ | ' ' |  |
| 36 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 37 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 38 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 39 | fdecisiontype | fdecisiontype | bpchar | 1 |  | √ | ' ' |  |
| 40 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 41 | fsubmitdate | fsubmitdate | timestamp | 0 |  |  | null |  |
| 42 | fnodename | fnodename | varchar | 50 |  | √ | ' ' |  |
| 43 | fsourcetypeid | fsourcetypeid | int8 | 64 |  | √ | 0 |  |
| 44 | fsrcbilltype | fsrcbilltype | varchar | 50 |  | √ | ' ' |  |
| 45 | fcurrentnode | fcurrentnode | int8 | 64 |  | √ | 0 |  |
| 46 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 47 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_project_ext_sid |  | fsourceid |
| 2 | pk_src_project_ext |  | fid |
| 3 | idx_src_project_ext_pid |  | fparentid |
| 4 | idx_src_project_ext_fid |  | fsrctypeid |

---

## 状态表分录-子表 t_src_project_ext_g

- **表名称：** 状态表分录-子表
- **表名：** t_src_project_ext_g

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftemplateid | 组件模板 | int8 | 64 |  | √ | 0 | [组件模板配置 pds_tplconfig](../pds_files/pds_tplconfig.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fbizstatus | 业务状态 | bpchar | 1 |  | √ | ' ' | 业务状态,枚举: A :未开始 B :处理中 C :已处理 D :已终止 Z :无需处理 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_project_ext_g |  | fid |
| 2 | idx_src_project_ext_g_cid |  | fcreatorid |
