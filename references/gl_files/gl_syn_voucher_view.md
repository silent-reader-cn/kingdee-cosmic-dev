# 凭证中间表-gl_syn_voucher_view

## 单据体-子表 t_gl_syn_voucherentry

- **表名称：** 单据体-子表
- **表名：** t_gl_syn_voucherentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faccountinfo | 会计科目（编码转JSON） | varchar | 255 |  | √ | ' ' | 会计科目（编码转JSON） |
| 3 | fcreditlocal | 本位币贷方金额 | numeric | 21 | 6 | √ | 0.000000 | 本位币贷方金额 |
| 4 | fmaincfiteminfo | 主表现金流量项目（编码转JSON） | varchar | 255 |  | √ | ' ' | 主表现金流量项目（编码转JSON） |
| 5 | fassgrpinfo | 核算维度（JSON） | varchar | 2000 |  | √ | ' ' | 核算维度（JSON） |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fmaincfamount | 主表项目金额 | numeric | 23 | 10 | √ | 0.0000000000 | 主表项目金额 |
| 8 | faccount | 会计科目（编码转id）（备用） | varchar | 255 |  | √ | ' ' | 会计科目（编码转id）（备用） |
| 9 | fcurrencyinfo | 币别（编码转JSON） | varchar | 255 |  | √ | ' ' | 币别（编码转JSON） |
| 10 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 11 | fentrydc | 分录方向 | varchar | 50 |  | √ | ' ' | 分录方向 |
| 12 | fexpiredate | 到期日 | timestamp | 0 |  |  | null | 到期日 |
| 13 | fedescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 14 | fquantity | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 15 | fcreditori | 原币贷方金额 | numeric | 21 | 6 | √ | 0.000000 | 原币贷方金额 |
| 16 | flocalrate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 17 | fsuppcfamount | 补充资料金额 | numeric | 23 | 10 | √ | 0.0000000000 | 补充资料金额 |
| 18 | fmeasureunitinfo | 计量单位（编码转JSON） | varchar | 255 |  | √ | ' ' | 计量单位（编码转JSON） |
| 19 | fdebitori | 原币借方金额 | numeric | 21 | 6 | √ | 0.000000 | 原币借方金额 |
| 20 | fdebitlocal | 本位币借方金额 | numeric | 21 | 6 | √ | 0.000000 | 本位币借方金额 |
| 21 | fbusinessnum | 业务编码 | varchar | 50 |  | √ | ' ' | 业务编码 |
| 22 | fassgrptext | 核算维度（新格式备用） | varchar | 2000 |  | √ | ' ' | 核算维度（新格式备用） |
| 23 | fmaincfassgrpinfo | 主表核算维度（JSON） | varchar | 2000 |  | √ | ' ' | 主表核算维度（JSON） |
| 24 | fsuppcfiteminfo | 补充资料项目（编码转JSON） | varchar | 255 |  | √ | ' ' | 补充资料项目（编码转JSON） |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_synvoucherentry |  | fid,faccountinfo |
| 2 | pk_t_gl_syn_voucherentry |  | fentryid |

---

## 凭证中间表-主表 t_gl_syn_voucher

- **表名称：** 凭证中间表-主表
- **表名：** t_gl_syn_voucher

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvouchertype | 凭证类型（编码转JSON） | varchar | 255 |  | √ | ' ' | 凭证类型（编码转JSON） |
| 3 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 4 | fissyn | 是否同步数据到苍穹凭证 | bpchar | 1 |  | √ | '0' | 是否同步数据到苍穹凭证 |
| 5 | fvoucherstatus | 导入凭证状态 | bpchar | 1 |  | √ | '0' | 导入凭证状态,枚举: A :暂存 B :提交 C :审核 F :复核 G :过账 |
| 6 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 7 | fbooktype | 账簿类型（编码转JSON） | varchar | 255 |  | √ | ' ' | 账簿类型（编码转JSON） |
| 8 | fattachmet | 附件数 | int8 | 64 |  | √ | 0 | 附件数 |
| 9 | fdescription | 参考信息 | varchar | 255 |  | √ | ' ' | 参考信息 |
| 10 | fbillno | 凭证号 | varchar | 30 |  | √ | ' ' | 凭证号 |
| 11 | forg | 组织（编码转JSON） | varchar | 255 |  | √ | ' ' | 组织（编码转JSON） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gl_syn_voucher |  | fid |
| 2 | idx_gl_synvoucher |  | fbillno |

---

## 子单据体-子表 t_gl_syn_subvoucherentry

- **表名称：** 子单据体-子表
- **表名：** t_gl_syn_subvoucherentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fvalue | 维度值 | varchar | 50 |  | √ | ' ' | 维度值 |
| 2 | ftype | 维度属性 | varchar | 50 |  | √ | ' ' | 维度属性 |
| 3 | fcashvalue | 现金流量值 | varchar | 50 |  | √ | ' ' | 现金流量值 |
| 4 | fkey | 维度键 | varchar | 50 |  | √ | ' ' | 维度键 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fothervalue | 预留文本 | varchar | 50 |  | √ | ' ' | 预留文本 |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gl_syn_subvoucherentry |  | fdetailid |
| 2 | idx_gl_subentry |  | fentryid |
