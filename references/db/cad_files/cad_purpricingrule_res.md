# 采购取价规则(资源)-cad_purpricingrule_res

## 采购取价规则(资源)-主表 t_cad_purpricingruleres

- **表名称：** 采购取价规则(资源)-主表
- **表名：** t_cad_purpricingruleres

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpricingqtyorder | 取量字段 | varchar | 30 |  | √ | ' ' | 取量字段,枚举: baseqty :基本数量 |
| 3 | fsubelementid | 取价成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 4 | fpricingdayorder | 取价天数 | int4 | 32 |  | √ | 0 | 取价天数 |
| 5 | fiswithcomporder | 考虑关联公司 | bpchar | 1 |  | √ | ' ' | 考虑关联公司 |
| 6 | fresauxpty | 资源对应物料辅助属性字段 | varchar | 30 |  | √ | ' ' | 资源对应物料辅助属性字段,枚举: |
| 7 | fresmatversion | 资源对应物料版本字段 | varchar | 30 |  | √ | ' ' | 资源对应物料版本字段,枚举: |
| 8 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fcalcbasis | 取价计算依据 | varchar | 30 |  | √ | ' ' | 取价计算依据,枚举: 001 :资源工时 002 :物料 003 :批次 |
| 10 | fresmat | 资源对应物料字段 | varchar | 30 |  | √ | ' ' | 资源对应物料字段,枚举: |
| 11 | fcosttypeid | 成本类型 | int8 | 64 |  | √ | 0 | 标准成本方案 cad_costtype |
| 12 | fpricingvalueorder | 取价字段 | varchar | 30 |  | √ | ' ' | 取价字段,枚举: amount :金额 |
| 13 | forgorderid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_purpricingruleres |  | fid |
| 2 | idx_cad_purpricingruleres |  | fcosttypeid |

---

## 采购组织-多选基础资料表 t_cad_res_purorg

- **表名称：** 采购组织-多选基础资料表
- **表名：** t_cad_res_purorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cad_res_purorg |  | fid,fbasedataid |
| 2 | pk_t_cad_res_purorg |  | fpkid |

---

## 单据类型-多选基础资料表 t_cad_res_billtypeorder

- **表名称：** 单据类型-多选基础资料表
- **表名：** t_cad_res_billtypeorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_res_billtypeorder |  | fpkid |
| 2 | idx_cad_res_billtypeorder |  | fid,fbasedataid |
