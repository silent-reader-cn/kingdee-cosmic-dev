# 即征即退软件映射-bd_levyrefundmap

## 物料分类-多选基础资料表 t_bd_lfmap_materialgroup

- **表名称：** 物料分类-多选基础资料表
- **表名：** t_bd_lfmap_materialgroup

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
| 1 | idx_bd_lfmap_materialgroup_fk |  | fid |
| 2 | pk_bd_lfmap_materialgroup |  | fpkid |

---

## 即征即退软件映射-多语言表 t_bd_levyrefundmap_l

- **表名称：** 即征即退软件映射-多语言表
- **表名：** t_bd_levyrefundmap_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_levyrefundmap_l_0 |  | fid,flocaleid |
| 2 | pk_bd_levyrefundmap_l |  | fpkid |

---

## 物料-多选基础资料表 t_bd_lfmap_material

- **表名称：** 物料-多选基础资料表
- **表名：** t_bd_lfmap_material

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_lfmap_material_fk |  | fid |
| 2 | pk_bd_lfmap_material |  | fpkid |

---

## 即征即退软件映射-主表 t_bd_levyrefundmap

- **表名称：** 即征即退软件映射-主表
- **表名：** t_bd_levyrefundmap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fmaterialgroup | fmaterialgroup | int8 | 64 |  | √ | 0 |  |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | flevyrefund | 即征即退软件 | int8 | 64 |  | √ | 0 | 即征即退软件 bd_levyrefund |
| 6 | fmaterialgroupstandard | 物料分类标准 | int8 | 64 |  | √ | 0 | 物料分类标准 bd_materialgroupstandard |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fitemclassfield | fitemclassfield | int8 | 64 |  | √ | 0 |  |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fitemclasstypefield | fitemclasstypefield | varchar | 30 |  | √ | ' ' |  |
| 13 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fmaterial | fmaterial | int8 | 64 |  | √ | 0 |  |
| 15 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_levyrefundmap |  | fid |
| 2 | idx_bd_levyrefundmap |  | fnumber |
