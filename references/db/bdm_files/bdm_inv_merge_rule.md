# 单据合并规则-bdm_inv_merge_rule

## 单据合并规则-多语言表 t_bdm_inv_merge_rule_l

- **表名称：** 单据合并规则-多语言表
- **表名：** t_bdm_inv_merge_rule_l

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
| 1 | pk_t_bdm_inv_merge_rule_l |  | fpkid |
| 2 | idx_bdm_merge_rule_l |  | fid,flocaleid |

---

## 单据合并规则-主表 t_bdm_inv_merge_rule

- **表名称：** 单据合并规则-主表
- **表名：** t_bdm_inv_merge_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fbillmergekey | 单据合并key | varchar | 300 |  | √ | ' ' | 单据合并key |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsamerowtypemerge | 同性质商品行合并处理 | varchar | 50 |  | √ | ' ' | 同性质商品行合并处理,枚举: 2 :数量置为1，反算单价 3 :数量、单价置空 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fnodeviationmergerule | 不允许尾差处理逻辑 | varchar | 50 |  | √ | ' ' | 不允许尾差处理逻辑,枚举: 1 :单据无法开票 2 :单据可开票，符合条件的数据合并成多行 |
| 9 | fdeviationrule | 尾差处理规则 | varchar | 50 |  | √ | ' ' | 尾差处理规则,枚举: 1 :单据总税额、总不含税金额、价税合计不允许尾差 2 :单据价税合计不允许尾差 |
| 10 | fitemmergekey | 明细合并key | varchar | 300 |  | √ | ' ' | 明细合并key |
| 11 | fdifferentrowtypemerge | 不同性质行合并处理 | varchar | 50 |  | √ | ' ' | 不同性质行合并处理,枚举: 1 :数量累加，反算单价 2 :数量置为1，反算单价 3 :数量、单价置空 4 :使用最终开票明细行原数量 |
| 12 | fitemmergename | 明细可变字段 | varchar | 600 |  | √ | ' ' | 明细可变字段 |
| 13 | fdeviationrewriterule | 有尾差重算逻辑 | varchar | 50 |  | √ | ' ' | 有尾差重算逻辑,枚举: 1 :可重新计算单价 |
| 14 | fremarkmergetype | fremarkmergetype | varchar | 50 |  | √ | '1' |  |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fnegativeoffset | 负数未完全冲抵 | varchar | 50 |  | √ | ' ' | 负数未完全冲抵,枚举: 1 :无法开票 2 :明细剩余金额与同税率的行合并 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fclearitemkey | fclearitemkey | varchar | 50 |  | √ | ' ' |  |
| 19 | fbillmergename | 单据合并名称显示 | varchar | 600 |  | √ | ' ' | 单据合并名称显示 |
| 20 | fenable | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :可用 |
| 21 | fsystempreset | 是否系统预置 | varchar | 50 |  | √ | ' ' | 是否系统预置,枚举: 1 :是 2 :否 |
| 22 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 23 | fclearitemname | fclearitemname | varchar | 100 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdm_merge_rule |  | fnumber |
| 2 | pk_t_bdm_inv_merge_rule |  | fid |
