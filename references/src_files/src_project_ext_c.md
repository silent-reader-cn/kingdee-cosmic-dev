# 扩展状态表C(标准预留)-src_project_ext_c

## 扩展状态表C(标准预留)-主表 t_src_project_ext

- **表名称：** 扩展状态表C(标准预留)-主表
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
| 9 | fsrctypeid | fsrctypeid | int8 | 64 |  | √ | 0 |  |
| 10 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 11 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 12 | fopentype | fopentype | bpchar | 1 |  | √ | ' ' |  |
| 13 | fsceneid | fsceneid | int8 | 64 |  | √ | 0 |  |
| 14 | fpurgroupid | fpurgroupid | int8 | 64 |  | √ | 0 |  |
| 15 | ftendertype | ftendertype | bpchar | 1 |  | √ | ' ' |  |
| 16 | fbiztypeid | fbiztypeid | int8 | 64 |  | √ | 0 |  |
| 17 | fismultipackage | fismultipackage | bpchar | 1 |  | √ | '0' |  |
| 18 | fsourceclassid | fsourceclassid | int8 | 64 |  | √ | 0 |  |
| 19 | fopenstatus | fopenstatus | bpchar | 1 |  | √ | '1' |  |
| 20 | fmanagetype | fmanagetype | bpchar | 1 |  | √ | ' ' |  |
| 21 | funauditorid | funauditorid | int8 | 64 |  | √ | 0 |  |
| 22 | ftaxtype | ftaxtype | varchar | 30 |  | √ | ' ' |  |
| 23 | fbillno | fbillno | varchar | 30 |  | √ | ' ' |  |
| 24 | fbidname | fbidname | varchar | 300 |  | √ | ' ' |  |
| 25 | fterminalnode | fterminalnode | int8 | 64 |  | √ | 0 |  |
| 26 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 27 | funsubmitterid | funsubmitterid | int8 | 64 |  | √ | 0 |  |
| 28 | funsubmitdate | funsubmitdate | timestamp | 0 |  |  | null |  |
| 29 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 30 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 31 | fparentid | fparentid | varchar | 50 |  | √ | ' ' |  |
| 32 | fsubmitterid | fsubmitterid | int8 | 64 |  | √ | 0 |  |
| 33 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 34 | fsrcbillid | fsrcbillid | varchar | 50 |  | √ | ' ' |  |
| 35 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 36 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 37 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 38 | fdecisiontype | fdecisiontype | bpchar | 1 |  | √ | ' ' |  |
| 39 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 40 | fsubmitdate | fsubmitdate | timestamp | 0 |  |  | null |  |
| 41 | fnodename | fnodename | varchar | 50 |  | √ | ' ' |  |
| 42 | fsourcetypeid | fsourcetypeid | int8 | 64 |  | √ | 0 |  |
| 43 | fsrcbilltype | fsrcbilltype | varchar | 50 |  | √ | ' ' |  |
| 44 | fcurrentnode | fcurrentnode | int8 | 64 |  | √ | 0 |  |
| 45 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 46 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

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

## 状态表分录-子表 t_src_project_ext_c

- **表名称：** 状态表分录-子表
- **表名：** t_src_project_ext_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftemplateid | 组件模板 | int8 | 64 |  | √ | 0 | 组件模板配置 pds_tplconfig |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
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
| 1 | idx_src_project_ext_c_cid |  | fcreatorid |
| 2 | pk_src_project_ext_c |  | fid |
