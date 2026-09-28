# 发票类型(发票云)-er_invoicetype

## 发票类型(发票云)-多语言表 t_er_invoicetype_l

- **表名称：** 发票类型(发票云)-多语言表
- **表名：** t_er_invoicetype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_invoicetype_l_fid |  | fid,flocaleid |
| 2 | pk_t_er_invoicetype_l |  | fpkid |

---

## 发票类型(发票云)-主表 t_er_invoicetype

- **表名称：** 发票类型(发票云)-主表
- **表名：** t_er_invoicetype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 3 | fisvatinvoice | 增值税发票 | bpchar | 1 |  | √ | '0' | 增值税发票 |
| 4 | fisoffset | 可抵扣 | bpchar | 1 |  | √ | '0' | 可抵扣 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fistransportinvoice | 运输票据 | bpchar | 1 |  | √ | '0' | 运输票据 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fuserdefinerule | 自定义条件json | varchar | 2000 |  | √ | ' ' | 自定义条件json |
| 9 | fjs | js文本 | varchar | 2000 |  | √ | ' ' | js文本 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 36 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fiseinvoice | 电子发票 | bpchar | 1 |  | √ | '0' | 电子发票 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fudrdisplay | 抵扣条件 | varchar | 2000 |  | √ | ' ' | 抵扣条件 |
| 16 | fisspecialinvoice | 专票 | bpchar | 1 |  | √ | '0' | 专票 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 19 | fisdefault | 是否预设 | bpchar | 1 |  | √ | '0' | 是否预设,枚举: 1 :是 0 :否 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_invoicetype |  | fid |
| 2 | idx_er_invoicetype_fnumber |  | fnumber |
