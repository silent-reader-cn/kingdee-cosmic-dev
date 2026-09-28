# 标准报表-fsa_stdrpts

## 包含报表项单据体-子表 t_fsa_stdrptent

- **表名称：** 包含报表项单据体-子表
- **表名：** t_fsa_stdrptent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frootcategory | 报表项类别一 | int8 | 64 |  | √ | 0 | 标准报表项目 fsa_rptitems |
| 3 | flevel | 层级 | int4 | 32 |  | √ | 0 | 层级 |
| 4 | fisleaf | 是否为叶子节点 | bpchar | 1 |  | √ | ' ' | 是否为叶子节点,枚举: 0 :非叶子节点 1 :叶子节点 |
| 5 | fitemtype | 报表项类型 | bpchar | 1 |  | √ | ' ' | 报表项类型,枚举: 1 :计算型 2 :展示型 3 :报表分类 |
| 6 | frootitemid | 根报表项的ID | int8 | 64 |  | √ | 0 | 根报表项的ID |
| 7 | fseqno | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | flongnumber | 长编码 | varchar | 100 |  | √ | ' ' | 长编码 |
| 9 | flineno | 行次 | int4 | 32 |  | √ | 0 | 行次 |
| 10 | frptitemid | 报表项ID | int8 | 64 |  | √ | 0 | 标准报表项目 fsa_rptitems |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fseccategory | 报表项类别二 | int8 | 64 |  | √ | 0 | 标准报表项目 fsa_rptitems |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fsa_stdrptent |  | fentryid |
| 2 | idx_fsa_stdent_fid |  | fid |
| 3 | idx_fsa_stdrptent1 |  | frptitemid,fitemtype |
| 4 | idx_fsa_stdrptent2 |  | flongnumber |

---

## 标准报表-多语言表 t_fsa_stdrpts_l

- **表名称：** 标准报表-多语言表
- **表名：** t_fsa_stdrpts_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fsa_stdrpts_l_fid |  | fid |
| 2 | pk_t_fsa_stdrpts_l |  | fpkid |

---

## 标准报表-主表 t_fsa_stdrpts

- **表名称：** 标准报表-主表
- **表名：** t_fsa_stdrpts

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 8 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 9 | frpttype | 报表类型 | bpchar | 1 |  | √ | ' ' | 报表类型,枚举: 0 :资产负债表 1 :利润表 2 :现金流量表 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fsa_stdrpts |  | fid |
| 2 | idx_fsa_stdrpts_2 |  | fstatus |
| 3 | idx_fsa_stdrpts_1 |  | fnumber,frpttype |
