# 成本BOM设置-scax_bomsetting

## 成本BOM设置-多语言表 t_scax_bomsetting_l

- **表名称：** 成本BOM设置-多语言表
- **表名：** t_scax_bomsetting_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_scax_bomsetting_l |  | fid,flocaleid |
| 2 | pk_scax_bomsetting_l |  | fpkid |

---

## 成本BOM设置-主表 t_scax_bomsetting

- **表名称：** 成本BOM设置-主表
- **表名：** t_scax_bomsetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbomtypeid | fbomtypeid | int8 | 64 |  | √ | 0 |  |
| 5 | flossformula | 损耗率计算公式 | varchar | 50 |  | √ | ' ' | 损耗率计算公式,枚举: 0 :不考虑 1 :子项标准用量 *（1 + 损耗率） 2 :子项标准用量 / (1 - 损耗率) |
| 6 | fconsidervalidperiod | 考虑子物料有效期 | bpchar | 1 |  | √ | ' ' | 考虑子物料有效期 |
| 7 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 10 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fmatcalcprop | 物料卷算属性 | bpchar | 1 |  | √ | ' ' | 物料卷算属性,枚举: A :自制 B :外购 C :委外 D :虚拟 |
| 13 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | [成本BOM scax_costbom](../scax_files/scax_costbom.md) |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fcosttypeid | 标准成本方案 | int8 | 64 |  | √ | 0 | [标准成本方案 cad_costtype](../basedata_files/cad_costtype.md) |
| 16 | fisdowncalc | 向下卷算 | bpchar | 1 |  | √ | ' ' | 向下卷算 |
| 17 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 18 | fconsideryieldrate | 考虑成品率 | bpchar | 1 |  | √ | ' ' | 考虑成品率 |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fconsiderstandardhour | fconsiderstandardhour | bpchar | 1 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_scax_bomsetting |  | fcosttypeid,fmaterialid |
| 2 | idx_scax_bomsetting_number |  | fbillno |
| 3 | pk_scax_bomsetting |  | fid |
