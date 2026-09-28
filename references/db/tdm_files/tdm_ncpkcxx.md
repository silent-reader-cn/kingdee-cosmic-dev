# 农产品库存信息-tdm_ncpkcxx

## 农产品库存信息-主表 t_tdm_ncpkcxx

- **表名称：** 农产品库存信息-主表
- **表名：** t_tdm_ncpkcxx

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fmaterialusage | 物料用途 | varchar | 50 |  | √ | ' ' | 物料用途,枚举: 1 :深加工 2 :直接销售 |
| 6 | fzzsse | 增值税税额 | numeric | 23 | 10 | √ | 0 | 增值税税额 |
| 7 | fqttzje | 其他调整金额 | numeric | 23 | 10 | √ | 0 | 其他调整金额 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fgsse | 关税税额 | numeric | 23 | 10 | √ | 0 | 关税税额 |
| 10 | fbusinesstype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型,枚举: 1 :采购 2 :销售 |
| 11 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 12 | forg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fnum | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 15 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fbusinessdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 19 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 21 | fmaterialname | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 22 | funit | 计量单位 | varchar | 50 |  | √ | ' ' | 计量单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_ncpkcxx_org |  | forg |
| 2 | pk_tdm_ncpkcxx |  | fid |

---

## 农产品库存信息-多语言表 t_tdm_ncpkcxx_l

- **表名称：** 农产品库存信息-多语言表
- **表名：** t_tdm_ncpkcxx_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_ncpkcxx_l_0 |  | fid,flocaleid |
| 2 | pk_tdm_ncpkcxx_l |  | fpkid |
