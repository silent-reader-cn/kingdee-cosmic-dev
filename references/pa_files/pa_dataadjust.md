# 数据调整-pa_dataadjust

## 数据调整-主表 t_pa_dataadjust

- **表名称：** 数据调整-主表
- **表名：** t_pa_dataadjust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核不通过 E :审核通过 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fperiodbasetype | 期间基础资料类型 | varchar | 50 |  | √ | ' ' | 期间基础资料类型,枚举: bd_period :会计期间 |
| 8 | fanalysissystemid | 分析体系 | int8 | 64 |  | √ | 0 | 分析体系 pa_anasystemsetting |
| 9 | fadjustjson | 调整表数据 | varchar | 255 |  | √ | ' ' | 调整表数据 |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | ffaildesc | 失败原因 | varchar | 255 |  | √ | ' ' | 失败原因 |
| 14 | fanalysismodelid | 分析模型 | int8 | 64 |  | √ | 0 | 分析模型 pa_analysismodel |
| 15 | fadjustdesc | 调整原因 | varchar | 255 |  | √ | ' ' | 调整原因 |
| 16 | fadjuststatus | 调整状态 | varchar | 50 |  | √ | ' ' | 调整状态,枚举: 1 :未调整 2 :已调整 0 :调整失败 3 :作废 4 :已冲销 |
| 17 | fperiodtype | 期间类型 | int8 | 64 |  | √ | 0 | 会计日历类型 bd_period_type |
| 18 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fadjustjson_tag | 调整表数据_详情 | text | 0 |  |  | null | 调整表数据_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pa_dataadjust |  | fid |
| 2 | idx_pa_dataadjust |  | fbillno |
