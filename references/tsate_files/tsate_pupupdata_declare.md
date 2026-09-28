# 申报弹框业务数据单据-tsate_pupupdata_declare

## 申报弹框业务数据单据-主表 t_tsate_pupupdata_declare

- **表名称：** 申报弹框业务数据单据-主表
- **表名：** t_tsate_pupupdata_declare

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpopupdata | 弹框数据 | varchar | 255 |  | √ | ' ' | 弹框数据 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fpopupdata_tag | 弹框数据_详情 | text | 0 |  |  | null | 弹框数据_详情 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fprojectname | 项目名称 | varchar | 100 |  | √ | ' ' | 项目名称 |
| 10 | fbusinessdata | 业务数据 | varchar | 255 |  | √ | ' ' | 业务数据 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fbusinessdata_tag | 业务数据_详情 | text | 0 |  |  | null | 业务数据_详情 |
| 13 | fnowpopup | 是否当前弹框 | bpchar | 1 |  | √ | '0' | 是否当前弹框 |
| 14 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 15 | fpupupstatus | 弹窗状态 | varchar | 50 |  | √ | ' ' | 弹窗状态,枚举: 0 :初始化 1 :已选择 2 :已使用 3 :废弃 |
| 16 | fsbbtype | 申报表类型 | varchar | 36 |  | √ | ' ' | 模板类型 tctb_template_type |
| 17 | fbillno | 弹窗编码 | varchar | 30 |  | √ | ' ' | 弹窗编码 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fchannel | 申报通道 | varchar | 36 |  | √ | ' ' | 模板类型 tctb_template_type |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tsate_pupd_sbbid |  | fsbbid |
| 2 | pk_tsate_pupupdata_declare |  | fid |
