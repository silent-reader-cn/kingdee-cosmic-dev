# 拆分配置-bdm_inv_split_rule

## 拆分配置-主表 t_bdm_inv_split_rule

- **表名称：** 拆分配置-主表
- **表名：** t_bdm_inv_split_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | felecommonlimitamount | 电子普票不含税限额 | numeric | 23 | 10 | √ | 0.0000000000 | 电子普票不含税限额 |
| 3 | frulecode | 编号 | varchar | 20 |  | √ | ' ' | 编号 |
| 4 | flistrule | 清单处理规则 | varchar | 50 |  | √ | ' ' | 清单处理规则,枚举: 2 :不生成清单，商品行超过发票最大允许行，新增一张发票 0 :商品行超发票最多允许行数时，开具成清单发票 1 :不管商品行是否超发票最多允许行数，强制开具成清单发票 |
| 5 | fitemsplitkey | 拆分字段 | varchar | 300 |  | √ | ' ' | 拆分字段 |
| 6 | fallelespeciallimitamount | 全电专票不含税限额 | numeric | 23 | 10 | √ | 0 | 全电专票不含税限额 |
| 7 | fdetailmergerule | 商品行合并规则 | varchar | 50 |  | √ | ' ' | 商品行合并规则,枚举: 0 :不合并 2 :商品税率、名称、规格型号、计量单位、单价一致时合并 |
| 8 | fdevlimitsplit | 不能超过金税盘限额 | bpchar | 1 |  | √ | ' ' | 不能超过金税盘限额 |
| 9 | fdetailsplitrule | 商品行拆分规则 | varchar | 50 |  | √ | ' ' | 商品行拆分规则,枚举: 0 :不拆分 1 :按数量拆分 |
| 10 | fitemsplitname | 拆分字段名称 | varchar | 600 |  | √ | ' ' | 拆分字段名称 |
| 11 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | flistlimitcommon | 普票清单行数 | int8 | 64 |  | √ | 0 | 普票清单行数 |
| 13 | ftotaltaxamtcountrule | 税额计算规则 | varchar | 50 |  | √ | ' ' | 税额计算规则,枚举: 1 :以系统计算为准，系统将调整误差 2 :以实际输入税额为准 |
| 14 | fquantitydecimallimit | 数量小数位限制 | int8 | 64 |  | √ | 0 | 数量小数位限制 |
| 15 | fpricedecimallimit | 单价小数位限制 | int8 | 64 |  | √ | 0 | 单价小数位限制 |
| 16 | fstatus | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 1 :启用 0 :禁用 |
| 17 | fcreatedate | 新建时间 | timestamp | 0 |  |  | null | 新建时间 |
| 18 | ffixedquantity | 强制固定数量 | bpchar | 1 |  | √ | ' ' | 强制固定数量 |
| 19 | fquantity | 固定商品数量 | int8 | 64 |  | √ | 1 | 固定商品数量 |
| 20 | fallelecommonlimitamount | 全电普票不含税限额 | numeric | 23 | 10 | √ | 0 | 全电普票不含税限额 |
| 21 | fupdatedate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 22 | fsplitlisttype | 负数冲抵行规则 | varchar | 50 |  | √ | ' ' | 负数冲抵行规则,枚举: 1 :冲抵金额时反算数量，单价以被冲抵正数商品单价为准 |
| 23 | flistlimitelecomm | 电子普票清单行数 | int8 | 64 |  | √ | 0 | 电子普票清单行数 |
| 24 | felespeciallimitamount | 电子专票不含税限额 | numeric | 23 | 10 | √ | 0.0000000000 | 电子专票不含税限额 |
| 25 | fnegativedetailrule | 负数冲抵行优先合并与正数商品行名称、税率、规格型号、计量单位 | bpchar | 1 |  | √ | ' ' | 负数冲抵行优先合并与正数商品行名称、税率、规格型号、计量单位 |
| 26 | finvoiceremarkrule | 发票头备注取值 | varchar | 50 |  | √ | ' ' | 发票头备注取值,枚举: 0 :取单据第一行备注 1 :叠加明细行备注 |
| 27 | fsplitwithamount | 指定不含税金额 | bpchar | 1 |  | √ | ' ' | 指定不含税金额 |
| 28 | fremarksplitregex | 备注换行符 | varchar | 50 |  | √ | ' ' | 备注换行符,枚举: , :, / :/ \ :\ \n :换行 |
| 29 | fpapercommonlimitamount | 纸质普票不含税限额 | numeric | 23 | 10 | √ | 0.0000000000 | 纸质普票不含税限额 |
| 30 | fremarkautodistinct | 备注是否自动去重 | bpchar | 1 |  | √ | ' ' | 备注是否自动去重 |
| 31 | fdetailquantitysplitrule | 商品行按数量拆分规则 | varchar | 50 |  | √ | ' ' | 商品行按数量拆分规则,枚举: 1 :拆分商品总数量不变，调整最后的商品单价 2 :单价不变，调整最后的商品数量 |
| 32 | fpaperspeciallimitamount | 纸质专票不含税限额 | numeric | 23 | 10 | √ | 0.0000000000 | 纸质专票不含税限额 |
| 33 | fitemsplittype | 拆分类型 | bpchar | 1 |  | √ | ' ' | 拆分类型 |
| 34 | flistlimitelespec | 电子专票清单行数 | int8 | 64 |  | √ | 0 | 电子专票清单行数 |
| 35 | frulename | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 36 | flistlimitspecial | 专票清单行数 | int8 | 64 |  | √ | 0 | 专票清单行数 |
| 37 | fdealnum | 数量位数处理 | varchar | 10 |  | √ | '1' | 数量位数处理,枚举: 1 :单行商品税额误差超过范围时，以系统计算为准 2 :单行商品税额误差超过范围时，强制保留数量位数，反算不含税单价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdm_inv_split_rule |  | frulecode |
| 2 | pk_bdm_inv_split_rule |  | fid |
