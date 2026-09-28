# 业务对象隐藏设置-xkbos_objecthideset

## 业务对象隐藏设置-主表 t_xkbas_objecthideset

- **表名称：** 业务对象隐藏设置-主表
- **表名：** t_xkbas_objecthideset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 业务对象名称 | varchar | 255 |  | √ | ' ' | 业务对象名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fmenuname | 菜单名称 | varchar | 255 |  | √ | ' ' | 菜单名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fobjectentityid | 隐藏业务对象ID | varchar | 50 |  | √ | ' ' | 隐藏业务对象ID |
| 7 | fispreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fbizappid | 所属应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 10 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | ftype | 隐藏类型 | bpchar | 1 |  | √ | ' ' | 隐藏类型,枚举: 0 :业务对象隐藏 1 :菜单隐藏 |
| 14 | fhideorgtype | 隐藏规则 | varchar | 50 |  | √ | ' ' | 隐藏规则,枚举: 0 :固定隐藏 1 :单组织隐藏 2 :多组织隐藏 3 :非简体中文隐藏 4 :海外环境隐藏 5 :非企业版升级隐藏 6 :非简/繁体中文隐藏 |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 17 | fobjectentity | 隐藏业务对象 | varchar | 50 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 18 | fmenuid | 菜单id | varchar | 36 |  | √ | ' ' | 菜单id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbas_objecthideset_num |  | fnumber |
| 2 | idx_t_obj_hide_fmenuid |  | fmenuid |
| 3 | pk_t_xkbas_objecthideset |  | fid |

---

## 业务对象隐藏设置-多语言表 t_xkbas_objecthideset_l

- **表名称：** 业务对象隐藏设置-多语言表
- **表名：** t_xkbas_objecthideset_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 业务对象名称 | varchar | 500 |  | √ | ' ' | 业务对象名称 |
| 3 | fmenuname | 菜单名称 | varchar | 255 |  | √ | ' ' | 菜单名称 |
| 4 | flocaleid | flocaleid | varchar | 100 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkbas_objecthideset_l |  | fpkid |
| 2 | idx_xkbas_objecthideset_l_id |  | fid |
