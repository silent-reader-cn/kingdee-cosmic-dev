# 成本更新记录单-cad_costupdatebill

## 成本更新记录单-主表 t_cad_costupdatebill

- **表名称：** 成本更新记录单-主表
- **表名：** t_cad_costupdatebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrccosttypeid | 源成本类型 | int8 | 64 |  | √ | 0 | 标准成本方案 cad_costtype |
| 3 | fistarmateffecdate | 考虑物料有效期 | bpchar | 1 |  | √ | '0' | 考虑物料有效期 |
| 4 | fissrcpreparhour | 考虑准备工时 | bpchar | 1 |  | √ | '0' | 考虑准备工时 |
| 5 | fistarauxproperty | 考虑辅助属性 | bpchar | 1 |  | √ | '0' | 考虑辅助属性 |
| 6 | fissrcyield | 考虑成品率 | bpchar | 1 |  | √ | '0' | 考虑成品率 |
| 7 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 11 | fissrcauxproperty | 考虑辅助属性 | bpchar | 1 |  | √ | '0' | 考虑辅助属性 |
| 12 | ftarcosttypeid | 目标成本类型 | int8 | 64 |  | √ | 0 | 标准成本方案 cad_costtype |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fistarlossrate | 考虑子项损耗率 | bpchar | 1 |  | √ | '0' | 考虑子项损耗率 |
| 17 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 18 | fistarmatvers | 考虑物料版本 | bpchar | 1 |  | √ | '0' | 考虑物料版本 |
| 19 | fissrcmateffecdate | 考虑物料有效期 | bpchar | 1 |  | √ | '0' | 考虑物料有效期 |
| 20 | ftextareafield | 多行文本 | varchar | 510 |  | √ | ' ' | 多行文本 |
| 21 | fistarpreparhour | 考虑准备工时 | bpchar | 1 |  | √ | '0' | 考虑准备工时 |
| 22 | fissrcmatvers | 考虑物料版本 | bpchar | 1 |  | √ | '0' | 考虑物料版本 |
| 23 | fistaryield | 考虑成品率 | bpchar | 1 |  | √ | '0' | 考虑成品率 |
| 24 | fissrclossrate | 考虑子项损耗率 | bpchar | 1 |  | √ | '0' | 考虑子项损耗率 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | ftextareafield1 | 多行文本1 | varchar | 510 |  | √ | ' ' | 多行文本1 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cad_costupdatebill_pkey |  | fid |
