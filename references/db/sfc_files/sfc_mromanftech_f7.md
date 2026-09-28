# 检修工序计划分录F7(废弃)-sfc_mromanftech_f7

## 检修工序计划分录F7(废弃)-主表 t_sfc_mromanftechentry

- **表名称：** 检修工序计划分录F7(废弃)-主表
- **表名：** t_sfc_mromanftechentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foprishandover | foprishandover | bpchar | 1 |  | √ | '0' |  |
| 3 | foprplanbegintime | foprplanbegintime | timestamp | 0 |  |  | null |  |
| 4 | foprsumactualhours | foprsumactualhours | numeric | 23 | 10 | √ | 0 |  |
| 5 | fopractualendtime | fopractualendtime | timestamp | 0 |  |  | null |  |
| 6 | foprremark | foprremark | varchar | 255 |  | √ | ' ' |  |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | foprworkhours | 计划消耗工时 | numeric | 23 | 10 | √ | 0 | 计划消耗工时 |
| 9 | foprstandardqty | foprstandardqty | numeric | 23 | 10 | √ | 0 |  |
| 10 | foprpageseq | foprpageseq | varchar | 50 |  | √ | ' ' |  |
| 11 | foprqty | foprqty | numeric | 23 | 10 | √ | 0 |  |
| 12 | foprtotaljunkqty | foprtotaljunkqty | numeric | 23 | 10 | √ | 0 |  |
| 13 | foprprofessionaid | 行业 | int8 | 64 |  | √ | 0 | 树形基础资料模板 mpdm_professiona |
| 14 | fmachiningtype | fmachiningtype | varchar | 50 |  | √ | ' ' |  |
| 15 | foprproductionqty | foprproductionqty | numeric | 23 | 10 | √ | 0 |  |
| 16 | foprassignorid | foprassignorid | int8 | 64 |  | √ | 0 |  |
| 17 | foprno | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 18 | foprworkcenterid | foprworkcenterid | int8 | 64 |  | √ | 0 |  |
| 19 | foprtaskid | foprtaskid | int8 | 64 |  | √ | 0 |  |
| 20 | foprworkshopid | foprworkshopid | int8 | 64 |  | √ | 0 |  |
| 21 | foprprocessgroupid | 工序组 | int8 | 64 |  | √ | 0 | 工序组(废弃) mpdm_progroup |
| 22 | foproperationid | foproperationid | int8 | 64 |  | √ | 0 |  |
| 23 | foprsourceentryid | foprsourceentryid | varchar | 50 |  | √ | ' ' |  |
| 24 | fopractualbegintime | fopractualbegintime | timestamp | 0 |  |  | null |  |
| 25 | foprwbsid | foprwbsid | int8 | 64 |  | √ | 0 |  |
| 26 | foprcustomhours | foprcustomhours | numeric | 23 | 10 | √ | 0 |  |
| 27 | foprworkhourunitid | 工时单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 28 | fecostcenterid | fecostcenterid | int8 | 64 |  | √ | 0 |  |
| 29 | foprcheckerid | foprcheckerid | int8 | 64 |  | √ | 0 |  |
| 30 | fopreffectivehours | fopreffectivehours | numeric | 23 | 10 | √ | 0 |  |
| 31 | foprmodifierid | foprmodifierid | int8 | 64 |  | √ | 0 |  |
| 32 | foprdescription | foprdescription | varchar | 50 |  | √ | ' ' |  |
| 33 | foprsourcetype | foprsourcetype | varchar | 50 |  | √ | ' ' |  |
| 34 | foperationunitid | foperationunitid | int8 | 64 |  | √ | 0 |  |
| 35 | foprorgid | foprorgid | int8 | 64 |  | √ | 0 |  |
| 36 | foprctrlstrategy | foprctrlstrategy | int8 | 64 |  | √ | 0 |  |
| 37 | foprinvalid | foprinvalid | bpchar | 1 |  | √ | '0' |  |
| 38 | foprfunctionlocationid | foprfunctionlocationid | int8 | 64 |  | √ | 0 |  |
| 39 | foprstudystatus | foprstudystatus | varchar | 50 |  | √ | ' ' |  |
| 40 | foprunitid | foprunitid | int8 | 64 |  | √ | 0 |  |
| 41 | foprplanfinishtime | foprplanfinishtime | timestamp | 0 |  |  | null |  |
| 42 | foprstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: A :创建 B :计划 C :计划确认 D :下达 E :开工 F :完工 G :关闭 H :部分完工 |
| 43 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 44 | foprworkgroupid | foprworkgroupid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrotechentry_fid |  | fid |
| 2 | pk_sfc_mromanftechentry |  | fentryid |
