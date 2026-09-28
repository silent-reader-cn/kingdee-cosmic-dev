# 凭证断号-gl_voucherbreakpoint

## 凭证断号-主表 t_gl_voucherbreakpoint

- **表名称：** 凭证断号-主表
- **表名：** t_gl_voucherbreakpoint

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fvoucherid | 凭证id | int8 | 64 |  | √ | 0 | 凭证id |
| 4 | fperiodid | 期间id | int8 | 64 |  | √ | 0 | 期间id |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'C' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fvoucherno | 调整前凭证号 | varchar | 80 |  | √ | ' ' | 调整前凭证号 |
| 10 | fvouchertypeid | 凭证字 | int8 | 64 |  | √ | 0 | 凭证字 gl_vouchertype |
| 11 | fadjusterid | 调整人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fadjustdate | 调整日期 | timestamp | 0 |  |  | null | 调整日期 |
| 14 | fbooktypeid | 账簿类型id | int8 | 64 |  | √ | 0 | 账簿类型id |
| 15 | fnewvoucherno | 调整后凭证号 | varchar | 80 |  | √ | ' ' | 调整后凭证号 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 18 | fcurvoucherno | 当前凭证号 | varchar | 80 |  |  | ' ' | 当前凭证号 |
| 19 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 20 | fisadjust | 是否已调整 | bpchar | 1 |  | √ | '0' | 是否已调整,枚举: 0 :未调整 1 :调整完并已同步凭证数据 2 :调整完并未同步凭证数据 |
| 21 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_voucherbreakpoint_vid |  | fvoucherid |
| 2 | idx_gl_voucherbreakpoint_obpc |  | forgid,fbooktypeid,fperiodid,fcurvoucherno |
| 3 | t_gl_voucherbreakpoint_pkey |  | fid |
