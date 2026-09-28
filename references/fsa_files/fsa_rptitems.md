# 标准报表项目-fsa_rptitems

## 标准报表项目-多语言表 t_fsa_rptitems_l

- **表名称：** 标准报表项目-多语言表
- **表名：** t_fsa_rptitems_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 报表项名称 | varchar | 100 |  | √ | ' ' | 报表项名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fsa_rptitems_l |  | fpkid |
| 2 | idx_fsa_rptit_l_fid |  | fid |

---

## 标准报表项目-主表 t_fsa_rptitems

- **表名称：** 标准报表项目-主表
- **表名：** t_fsa_rptitems

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | frptitemsrctype | 报表项来源类型 | bpchar | 1 |  | √ | ' ' | 报表项来源类型,枚举: 0 :系统预置 1 :自定义 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | frootcategory | 报表项分类一 | int8 | 64 |  | √ | 0 | 标准报表项目 fsa_rptitems |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fitemtype | 报表项类型 | bpchar | 1 |  | √ | ' ' | 报表项类型,枚举: 1 :计算型 2 :展示型 3 :报表分类 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fnumber | 报表项编码 | varchar | 30 |  | √ | ' ' | 报表项编码 |
| 13 | frpttype | 所属报表 | bpchar | 1 |  | √ | ' ' | 所属报表,枚举: 0 :资产负债表 1 :利润表 2 :现金流量表 |
| 14 | fseccategory | 报表项分类二 | int8 | 64 |  | √ | 0 | 标准报表项目 fsa_rptitems |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fsa_rptitems_1 |  | fnumber,fitemtype,frpttype |
| 2 | pk_t_fsa_rptitems |  | fid |
| 3 | idx_fsa_rptitems_2 |  | fstatus,frptitemsrctype |
