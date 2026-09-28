# 卷算变更记录-cad_calchangerecord

## 卷算变更记录-主表 t_cad_calchangerecord

- **表名称：** 卷算变更记录-主表
- **表名：** t_cad_calchangerecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fsrcbillno | 来源单据编码 | varchar | 80 |  | √ | ' ' | 来源单据编码 |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fbusinessbill | 来源单据 | varchar | 30 |  | √ | ' ' | 来源单据,枚举: cad_purprices :外购物料标准价目表 cad_resourcerate :资源标准费用价目表 cad_outsourceprice :产品委外标准价目表 cad_bomsetting :成本BOM设置 cad_routersetting :成本工艺路线设置 |
| 8 | faudittime | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmatversid | 物料版本 | int8 | 64 |  | √ | 0 | [BOM版本 bd_bomversion](../basedata_files/bd_bomversion.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 处理状态 | varchar | 30 |  | √ | ' ' | 处理状态,枚举: A :待处理 B :处理中 C :已处理 D :处理异常 |
| 12 | fchangeop | 变更来源操作 | varchar | 30 |  | √ | ' ' | 变更来源操作,枚举: audit :审核 unaudit :反审核 doprice :采购取价 refreshdata :刷新基础资料 stdratesetting :标准费率设置 enable :启用 disable :禁用 sync :同步数据 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fcosttypeid | 成本类型 | int8 | 64 |  | √ | 0 | [标准成本方案 cad_costtype](../basedata_files/cad_costtype.md) |
| 15 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | [辅助属性定义 bd_auxproperty](../sbd_files/bd_auxproperty.md) |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_cad_calchange_time |  | fstatus,fcreatetime |
| 2 | index_cad_calchange_id |  | fmaterialid,fcosttypeid |
| 3 | pk_t_cad_calchangerecord |  | fid |
