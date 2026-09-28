# 供应组织分配方案定义-mds_siteschemedef

## 供应组织分配方案定义-多语言表 t_mds_siteschemedef_l

- **表名称：** 供应组织分配方案定义-多语言表
- **表名：** t_mds_siteschemedef_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_y_mds_siteschemedef_l |  | fid,flocaleid |
| 2 | pk_t_mds_siteschemedef_l |  | fpkid |

---

## 供应组织分配方案定义-主表 t_mds_siteschemedef

- **表名称：** 供应组织分配方案定义-主表
- **表名：** t_mds_siteschemedef

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fsalorderstid | 待分配数据 | int8 | 64 |  | √ | 0 | [数据源配置 mrp_resource_dataconf_rgt](../msplan_files/mrp_resource_dataconf_rgt.md) |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fdataversionid | 数据版本 | int8 | 64 |  | √ | 0 | [数据版本 msplan_ds_version](../msplan_files/msplan_ds_version.md) |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fsetoffsettingid | 预测冲减定义 | int8 | 64 |  | √ | 0 | [预测冲减定义 mds_setoffsetting](../mds_files/mds_setoffsetting.md) |
| 11 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fisquota | 需求配额 | bpchar | 1 |  | √ | '0' | 需求配额 |
| 13 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 14 | fdummysiteid | 缺配额组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fsitebasedataid | 供应类型 | int8 | 64 |  | √ | 0 | [供应组织分配供应定义 mds_sitebasedata](../mds_files/mds_sitebasedata.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_y_mds_siteschemedef |  | fnumber |
| 2 | pk_t_mds_siteschemedef |  | fid |

---

## 整机类型-多选基础资料表 t_mds_materialgpentry

- **表名称：** 整机类型-多选基础资料表
- **表名：** t_mds_materialgpentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mds_materialgpentry |  | fpkid |
| 2 | idx_y_mds_materialgpentry |  | fid,fbasedataid |
