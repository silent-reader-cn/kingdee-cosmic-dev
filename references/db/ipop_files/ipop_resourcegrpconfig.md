# 资源分组配置-ipop_resourcegrpconfig

## 分组配置单据体-子表 t_ipop_groupentity

- **表名称：** 分组配置单据体-子表
- **表名：** t_ipop_groupentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fgroupname | 分组名称 | varchar | 50 |  | √ | ' ' | 分组名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ipop_groupentity |  | fentryid |
| 2 | idx_ipop_groupentity_id |  | fid |

---

## 分组内模块-多选基础资料表 t_ipop_groupmodule

- **表名称：** 分组内模块-多选基础资料表
- **表名：** t_ipop_groupmodule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [资源清单明细 ipop_resoucelistdetail](../ipop_files/ipop_resoucelistdetail.md) |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ipop_groupmodule |  | fpkid |
| 2 | idx_ipop_groupmodule_entryid |  | fentryid |

---

## 资源分组配置-主表 t_ipop_resourcegrpconfig

- **表名称：** 资源分组配置-主表
- **表名：** t_ipop_resourcegrpconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fstatus | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fproductid | 产品系列 | int8 | 64 |  | √ | 0 | [资源辅助资料 ipop_resauxiliarydata](../ipop_files/ipop_resauxiliarydata.md) |
| 8 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fprodseriessn | fprodseriessn | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ipop_resourcegrpconfig_product |  | fproductid |
| 2 | pk_ipop_resourcegrpconfig |  | fid |
