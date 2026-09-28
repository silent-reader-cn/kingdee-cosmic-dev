# 工卡工艺分录F7选择-mpdm_mrocardoperation_f7

## 工卡工艺分录F7选择-主表 t_mpdm_mentryroute

- **表名称：** 工卡工艺分录F7选择-主表
- **表名：** t_mpdm_mentryroute

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fproductionworkshopid | fproductionworkshopid | int8 | 64 |  | √ | 0 |  |
| 3 | ffirstcheck | ffirstcheck | bpchar | 1 |  | √ | '0' |  |
| 4 | ftaxrate | ftaxrate | int8 | 64 |  | √ | 0 |  |
| 5 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 6 | foperationqty | foperationqty | numeric | 23 | 10 | √ | 0 |  |
| 7 | fchecktype | fchecktype | varchar | 50 |  | √ | ' ' |  |
| 8 | fbasebatchqty | fbasebatchqty | numeric | 23 | 10 | √ | 0 |  |
| 9 | foperationid | foperationid | int8 | 64 |  | √ | 0 |  |
| 10 | fprocessgroup | 工序组 | int8 | 64 |  | √ | 0 | [工序组(废弃) mpdm_progroup](../mpdm_files/mpdm_progroup.md) |
| 11 | fcardid | 工卡ID | int8 | 64 |  | √ | 0 | 工卡ID |
| 12 | fversionid | fversionid | int8 | 64 |  | √ | 0 |  |
| 13 | fpageseq1 | 页码 | varchar | 50 |  | √ | ' ' | 页码 |
| 14 | fsplitqty | fsplitqty | numeric | 23 | 10 | √ | 0 |  |
| 15 | foperationunitid | foperationunitid | int8 | 64 |  | √ | 0 |  |
| 16 | fpurchaseorgid | fpurchaseorgid | int8 | 64 |  | √ | 0 |  |
| 17 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 18 | fheadqty | fheadqty | numeric | 23 | 10 | √ | 0 |  |
| 19 | fworkstation | fworkstation | int8 | 64 |  | √ | 0 |  |
| 20 | foperationdesc | 工序说明 | varchar | 50 |  | √ | ' ' | 工序说明 |
| 21 | foverlaptimeunit | foverlaptimeunit | varchar | 50 |  | √ | ' ' |  |
| 22 | ftimeunit | ftimeunit | varchar | 50 |  | √ | ' ' |  |
| 23 | fisprocessoverlap | fisprocessoverlap | bpchar | 1 |  | √ | '0' |  |
| 24 | fprofessiona | 专业 | int8 | 64 |  | √ | 0 | [树形基础资料模板 mpdm_professiona](../mpdm_files/mpdm_professiona.md) |
| 25 | fcurrencyfield | fcurrencyfield | int8 | 64 |  | √ | 0 |  |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | foperationno | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 28 | foverlapqty | foverlapqty | numeric | 23 | 10 | √ | 0 |  |
| 29 | fpurchasegroupid | fpurchasegroupid | int8 | 64 |  | √ | 0 |  |
| 30 | fcustomhours | fcustomhours | numeric | 23 | 10 | √ | 0 |  |
| 31 | ftaxprice | ftaxprice | numeric | 23 | 10 | √ | 0 |  |
| 32 | fprice | fprice | numeric | 23 | 10 | √ | 0 |  |
| 33 | fmachiningtype | 加工类型 | varchar | 50 |  | √ | ' ' | 加工类型,枚举: 1001 :厂内加工 1002 :委外加工 1003 :内协加工 1004 :不限制 |
| 34 | foverlapunitid | foverlapunitid | int8 | 64 |  | √ | 0 |  |
| 35 | ffloorratio | ffloorratio | numeric | 23 | 10 | √ | 0 |  |
| 36 | fentrymaterialid | fentrymaterialid | int8 | 64 |  | √ | 0 |  |
| 37 | fworkcenterid | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心定义(废弃) mpdm_workcentre](../mpdm_files/mpdm_workcentre.md) |
| 38 | fminoverlaptime | fminoverlaptime | numeric | 23 | 10 | √ | 0 |  |
| 39 | fstandardhours | fstandardhours | numeric | 23 | 10 | √ | 0 |  |
| 40 | fminworktime | fminworktime | numeric | 23 | 10 | √ | 0 |  |
| 41 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 42 | fparentid | 工序序列 | varchar | 50 |  | √ | ' ' | 工序序列 |
| 43 | fsettlementcoefficient | fsettlementcoefficient | numeric | 23 | 10 | √ | 0 |  |
| 44 | fissplit | fissplit | bpchar | 1 |  | √ | '0' |  |
| 45 | fpurchasepersonid | fpurchasepersonid | int8 | 64 |  | √ | 0 |  |
| 46 | foprctrlstrategy | 工序控制策略 | int8 | 64 |  | √ | 0 | [工序控制策略(废弃) mpdm_proctrlstrategy](../mpdm_files/mpdm_proctrlstrategy.md) |
| 47 | fbottleprocedure | fbottleprocedure | bpchar | 1 |  | √ | '0' |  |
| 48 | fproductionorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 49 | fheadunitid | fheadunitid | int8 | 64 |  | √ | 0 |  |
| 50 | fupperratio | fupperratio | numeric | 23 | 10 | √ | 0 |  |
| 51 | fismilestoneprocess | fismilestoneprocess | bpchar | 1 |  | √ | '0' |  |
| 52 | fcollaborative | fcollaborative | bpchar | 1 |  | √ | '0' |  |
| 53 | fsettlementunitid | fsettlementunitid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_mentryroute |  | fentryid |
| 2 | idx_t_mpdm_mentryroute |  | fid |
