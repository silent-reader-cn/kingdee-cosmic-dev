# 成本明细方案F7-pds_costdetailtplf7

## 标的-多选基础资料表 t_pds_cost_purlist

- **表名称：** 标的-多选基础资料表
- **表名：** t_pds_cost_purlist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 成本项目 pds_costitem |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_cost_purlist_fid |  | fid |
| 2 | pk_pds_cost_purlist |  | fpkid |
| 3 | idx_pds_cost_purlist_bid |  | fbasedataid |

---

## 品类-多选基础资料表 t_pds_cost_category

- **表名称：** 品类-多选基础资料表
- **表名：** t_pds_cost_category

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_cost_category |  | fpkid |
| 2 | idx_pds_cost_category_bid |  | fbasedataid |
| 3 | idx_pds_cost_category_fid |  | fid |

---

## 成本明细方案F7-主表 t_pds_costdetailtpl

- **表名称：** 成本明细方案F7-主表
- **表名：** t_pds_costdetailtpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 3 | fpriority | fpriority | int4 | 32 |  | √ | 0 |  |
| 4 | fpurlistid | fpurlistid | int8 | 64 |  | √ | 0 |  |
| 5 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 6 | fmatchfield | 匹配字段数 | int4 | 32 |  | √ | 0 | 匹配字段数 |
| 7 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 8 | fcategoryid | fcategoryid | int8 | 64 |  | √ | 0 |  |
| 9 | fissyspreset | fissyspreset | bpchar | 1 |  | √ | '0' |  |
| 10 | fbillno | 方案编码 | varchar | 30 |  | √ | ' ' | 方案编码 |
| 11 | ftemplate | 组件模板 | int8 | 64 |  | √ | 0 | 组件模板配置 pds_tplconfig |
| 12 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 13 | fisv_id | fisv_id | varchar | 50 |  | √ | ' ' |  |
| 14 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 15 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 16 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 17 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :创建 B :审核中 C :已审核 D :重新审核 |
| 18 | fparentid | fparentid | varchar | 50 |  | √ | ' ' |  |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 21 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 22 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 23 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 24 | fcostdetailtplid | fcostdetailtplid | int8 | 64 |  | √ | 0 |  |
| 25 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_costdetailtpl_pid |  | fprojectid |
| 2 | pk_pds_costdetailtpl |  | fid |
| 3 | idx_pds_costdetailtpl_fbillno |  | fbillno |

---

## 寻源流程-多选基础资料表 t_pds_cost_srctype

- **表名称：** 寻源流程-多选基础资料表
- **表名：** t_pds_cost_srctype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 流程配置 pds_flowconfig |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_cost_srctype |  | fpkid |
| 2 | idx_pds_cost_srctype_fid |  | fid |
| 3 | idx_pds_cost_srctype_bid |  | fbasedataid |

---

## 寻源方式-多选基础资料表 t_pds_cost_sourcetype

- **表名称：** 寻源方式-多选基础资料表
- **表名：** t_pds_cost_sourcetype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_cost_sourcetype |  | fpkid |
| 2 | idx_pds_cost_sourcetype_fid |  | fid |
| 3 | idx_pds_cost_sourcetype_bid |  | fbasedataid |
