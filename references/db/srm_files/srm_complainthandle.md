# 投诉处理-srm_complainthandle

## 投诉处理-主表 t_srm_complaintmanage

- **表名称：** 投诉处理-主表
- **表名：** t_srm_complaintmanage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flaunchemail | 投诉人邮箱 | varchar | 100 |  | √ | ' ' | 投诉人邮箱 |
| 3 | fdealorgid | 指派处理组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | facceptuserid | 受理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fdealback | 处理回复 | varchar | 2000 |  | √ | ' ' | 处理回复 |
| 6 | flaunchphone | 投诉人手机号 | varchar | 50 |  | √ | ' ' | 投诉人手机号 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcomplaintstatus | 发起投诉单投诉状态 | varchar | 10 |  | √ | ' ' | 发起投诉单投诉状态,枚举: A :待受理 B :处理中 C :已完成 |
| 9 | fstatus | 投诉管理单据状态 | varchar | 10 |  | √ | ' ' | 投诉管理单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已指派 |
| 10 | fcomplaintdetail | 投诉详情 | varchar | 2000 |  | √ | ' ' | 投诉详情 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fprecomments | 初步处理意见 | varchar | 10 |  | √ | ' ' | 初步处理意见,枚举: A :受理 B :不予受理 |
| 13 | fcomplaintcompany | 被投诉公司 | varchar | 100 |  | √ | ' ' | 被投诉公司 |
| 14 | fmanagecomplaintstatus | 投诉管理投诉状态 | varchar | 10 |  | √ | ' ' | 投诉管理投诉状态,枚举: A :待受理 B :处理中 C :结果发布 D :结果提交 |
| 15 | fdealuserid | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fsolvedate | 期望解决日期 | timestamp | 0 |  |  | null | 期望解决日期 |
| 17 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 18 | fname | 投诉主题 | varchar | 255 |  | √ | ' ' | 投诉主题 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fbillstatus | 发起投诉单据状态 | varchar | 10 |  | √ | ' ' | 发起投诉单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fsupplierid | 发起供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 24 | fcomplaintuser | 被投诉人 | varchar | 100 |  | √ | ' ' | 被投诉人 |
| 25 | flaunchuserid | 投诉发起人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fhandlestatus | 单据状态 | varchar | 10 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | fexplain | 说明 | varchar | 512 |  | √ | ' ' | 说明 |
| 29 | flaunchdate | 投诉发起日期 | timestamp | 0 |  |  | null | 投诉发起日期 |
| 30 | fhandlecomplaintstatus | 投诉状态 | varchar | 10 |  | √ | ' ' | 投诉状态,枚举: A :待处理 B :结果提交 C :结果发布 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_complaintmanage_handles |  | fhandlestatus |
| 2 | idx_complaintmanage_status |  | fstatus |
| 3 | pk_t_srm_complaintmanage |  | fid |
| 4 | idx_complaintmanage_supid |  | fsupplierid |
| 5 | idx_complaintmanage_manage |  | fmanagecomplaintstatus |
| 6 | idx_complaintmanage_billstatus |  | fbillstatus |
