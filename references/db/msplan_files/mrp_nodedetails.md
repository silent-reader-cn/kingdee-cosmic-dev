# 节点详情-mrp_nodedetails

## 参与MRP库存类型-多选基础资料表 t_mrp_invstocktype

- **表名称：** 参与MRP库存类型-多选基础资料表
- **表名：** t_mrp_invstocktype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_invstocktype |  | fpkid |
| 2 | idx_mrp_invstocktype_fk |  | fid |

---

## 库存供应组织设置-子表 t_mrp_stocksorgentry

- **表名称：** 库存供应组织设置-子表
- **表名：** t_mrp_stocksorgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fintegerfield | 组织供货优先级 | int8 | 64 |  | √ | 0 | 组织供货优先级 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fstorageorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fdecimalfield | 库存可供比例 | numeric | 23 | 10 | √ | 0.0000000000 | 库存可供比例 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_stocksorgentry |  | fid,fseq |
| 2 | pk_t_mrp_stocksorgentry |  | fentryid |

---

## 仓库设置单据体-子表 t_mrp_stocksetup

- **表名称：** 仓库设置单据体-子表
- **表名：** t_mrp_stocksetup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpriority | 仓库供货优先级 | int8 | 64 |  | √ | 0 | 仓库供货优先级 |
| 3 | fstocknumberid | 仓库编码 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fiswastewh | 三品库 | bpchar | 1 |  | √ | '0' | 三品库 |
| 6 | fstorageaddress | fstorageaddress | varchar | 50 |  | √ | ' ' |  |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fstockorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fstockindexid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_stocksetup |  | fid,fseq |
| 2 | pk_t_mrp_stocksetup |  | fentryid |

---

## 物料设置-子表 t_mrp_materialsetup

- **表名称：** 物料设置-子表
- **表名：** t_mrp_materialsetup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpriority | 供货优先级 | int8 | 64 |  | √ | 0 | 供货优先级 |
| 4 | fparentbasedatafield | fparentbasedatafield | int8 | 64 |  | √ | 0 |  |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 7 | fstockid | 仓库编码 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 8 | fmaterielid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fstockindexid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 11 | fstockratio | 库存可供比例 | numeric | 23 | 10 | √ | 0.0000000000 | 库存可供比例 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_materialsetup |  | fentryid |
| 2 | idx_mrp_materialsetup |  | fid,fseq |

---

## 组织和仓库展示单据体-子表 t_mrp_showentity

- **表名称：** 组织和仓库展示单据体-子表
- **表名：** t_mrp_showentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstorageorg | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpriority | 供货优先级 | int4 | 32 |  | √ | 0 | 供货优先级 |
| 4 | fstocknumber | 仓库编码 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fsupplypriority | 仓库供货优先级 | int4 | 32 |  | √ | 0 | 仓库供货优先级 |
| 7 | forgsetid | 组织设置单据体id | varchar | 50 |  | √ | ' ' | 组织设置单据体id |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fstockscale | 库存可供比例 | numeric | 23 | 10 | √ | 0 | 库存可供比例 |
| 10 | fstockindex | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 11 | fwastewarehouse | 三品库 | bpchar | 1 |  | √ | '0' | 三品库 |
| 12 | fstocksetupentryentityid | 仓库设置单据体id | varchar | 50 |  | √ | ' ' | 仓库设置单据体id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_showentity |  | fentryid |
| 2 | idx_mrp_showentity_fk |  | fid |

---

## 节点详情-主表 t_mrp_nodedetails

- **表名称：** 节点详情-主表
- **表名：** t_mrp_nodedetails

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparentdnyid | 父对象id | varchar | 50 |  | √ | ' ' | 父对象id |
| 3 | fsupplyorggrouptext_tag | 供应组织分类存储_详情 | text | 0 |  |  | null | 供应组织分类存储_详情 |
| 4 | fbodtime | 运输周期（天） | int4 | 32 |  | √ | 0 | 运输周期（天） |
| 5 | fstocksetup | 仓库运算范围 | varchar | 30 |  | √ | ' ' | 仓库运算范围,枚举: 1 :全部仓库 2 :指定仓库 3 :排除指定仓库 |
| 6 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 7 | fstockdemandorg | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fnodenumber | 节点编码 | varchar | 50 |  | √ | ' ' | 节点编码 |
| 9 | fsupplyorggrouptext | 供应组织分类存储 | varchar | 255 |  | √ | ' ' | 供应组织分类存储 |
| 10 | fdemandorgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_nodedetails |  | fid |
| 2 | idx_mrp_nodedetails_fk |  | fparentdnyid |

---

## 参与MRP库存状态-多选基础资料表 t_mrp_invstockstatus

- **表名称：** 参与MRP库存状态-多选基础资料表
- **表名：** t_mrp_invstockstatus

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_invstockstatus |  | fpkid |
| 2 | idx_mrp_invstockstatus_fk |  | fid |

---

## 供应组织单据体存储-子表 t_mrp_definitionorgentry

- **表名称：** 供应组织单据体存储-子表
- **表名：** t_mrp_definitionorgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fsupplyorgtypeid | 供应组织分类 | int8 | 64 |  | √ | 0 | [供应组织分类 mrp_orgtpy](../msplan_files/mrp_orgtpy.md) |
| 4 | fsupplyrule | 供应规则 | varchar | 30 |  | √ | ' ' | 供应规则,枚举: 1 :跨组织领料 2 :跨组织调拨 3 :跨组织入库 |
| 5 | fsupplyorgid | 供应组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fsupplyproportion | 供应比例 | numeric | 23 | 10 | √ | 0.0000000000 | 供应比例 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_definitionorgentry |  | fid,fseq |
| 2 | pk_t_mrp_definitionorgentry |  | fentryid |

---

## 默认供应设置-子表 t_mrp_defaultsupply

- **表名称：** 默认供应设置-子表
- **表名：** t_mrp_defaultsupply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fsupplyrule | 供应规则 | varchar | 30 |  | √ | ' ' | 供应规则,枚举: 1 :跨组织领料 2 :跨组织调拨 3 :跨组织入库 |
| 4 | fsupplyorgid | 供应组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fsupplyratio | 供应比例 | numeric | 23 | 10 | √ | 0 | 供应比例 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_defaultsupply_fk |  | fid |
| 2 | pk_mrp_defaultsupply |  | fentryid |

---

## 物料设置单据体存储-子表 t_mrp_definitionentry

- **表名称：** 物料设置单据体存储-子表
- **表名：** t_mrp_definitionentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsupplytypeid | 供应组织分类 | int8 | 64 |  | √ | 0 | [供应组织分类 mrp_orgtpy](../msplan_files/mrp_orgtpy.md) |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_definitionentry |  | fid,fseq |
| 2 | pk_t_mrp_definitionentry |  | fentryid |
