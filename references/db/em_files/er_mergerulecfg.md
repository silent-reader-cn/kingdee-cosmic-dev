# 手动合并规则-er_mergerulecfg

## 手动合并规则-多语言表 t_er_mergerulecfg_l

- **表名称：** 手动合并规则-多语言表
- **表名：** t_er_mergerulecfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fid_er_mergerulecfg_l |  | fid |
| 2 | pk_er_mergerulecfg_l |  | fpkid |

---

## 手动合并规则-主表 t_er_mergerulecfg

- **表名称：** 手动合并规则-主表
- **表名：** t_er_mergerulecfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisinvoicetype | 发票类型相同 | bpchar | 1 |  | √ | '0' | 发票类型相同 |
| 3 | ftaxrate | 税率相同 | bpchar | 1 |  | √ | '0' | 税率相同 |
| 4 | fistrip2to | 目的地相同 | bpchar | 1 |  | √ | '0' | 目的地相同 |
| 5 | fuserdefinerule | 自定义条件json | varchar | 2000 |  | √ | ' ' | 自定义条件json |
| 6 | fisentrycurrency | 币种相同 | bpchar | 1 |  | √ | '0' | 币种相同 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fisinvoice | 发票相同 | bpchar | 1 |  | √ | '0' | 发票相同 |
| 9 | fisentrycostcompany | 费用承担公司相同 | bpchar | 1 |  | √ | '0' | 费用承担公司相同 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fudrdisplay | 自定义 | varchar | 2000 |  | √ | ' ' | 自定义 |
| 14 | fisexpenseitem | 费用项目相同 | bpchar | 1 |  | √ | '0' | 费用项目相同 |
| 15 | fistriptime | 行程期间相同 | bpchar | 1 |  | √ | '0' | 行程期间相同 |
| 16 | fistripitem | 差旅项目相同 | bpchar | 1 |  | √ | '0' | 差旅项目相同 |
| 17 | fisentrycostdept | 费用承担部门相同 | bpchar | 1 |  | √ | '0' | 费用承担部门相同 |
| 18 | fistrip2travelers | 出差人相同 | bpchar | 1 |  | √ | '0' | 出差人相同 |
| 19 | fistrip2from | 出发地相同 | bpchar | 1 |  | √ | '0' | 出发地相同 |
| 20 | fisoffset | 可抵扣相同 | bpchar | 1 |  | √ | '0' | 可抵扣相同 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fseatgrade | 座位等级相同 | bpchar | 1 |  | √ | '0' | 座位等级相同 |
| 25 | fisreimburser | 报销人相同 | bpchar | 1 |  | √ | '0' | 报销人相同 |
| 26 | fjs | js文本 | varchar | 2000 |  | √ | ' ' | js文本 |
| 27 | fenable | 使用状态 | varchar | 10 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 29 | fbilltype | 单据类型 | varchar | 30 |  | √ | ' ' | 单据类型,枚举: er_tripreimbursebill_card :差旅报销单 er_tripreimbursebill :差旅报销单（表） er_dailyreimbursebill :费用报销单 er_publicreimbursebill :对公报销单 |
| 30 | fiscostcenter | 成本中心相同 | bpchar | 1 |  | √ | '0' | 成本中心相同 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fnumber_er_mergerulecfg |  | fnumber |
| 2 | pk_er_mergerulecfg |  | fid |
