# 变更对象-plm_rm_changeobj

## 变更对象-主表 t_plm_rm_changeobj

- **表名称：** 变更对象-主表
- **表名：** t_plm_rm_changeobj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fchangeobj | 变更对象 | int8 | 64 |  | √ | 0 | 变更对象 |
| 3 | fchangeobjversionlock | 临时版本 | varchar | 50 |  | √ | ' ' | 临时版本 |
| 4 | fchangeobjtempid | 变更对象临时版本id | varchar | 50 |  | √ | ' ' | 变更对象临时版本id |
| 5 | fchangeobjbasedataid | 变更对象基础资料id | varchar | 50 |  | √ | ' ' | 变更对象基础资料id |
| 6 | fchangeobjreason | 申请变更原因 | varchar | 255 |  | √ | ' ' | 申请变更原因 |
| 7 | fchangeobjmaster | 变更对象内码 | int8 | 64 |  | √ | 0 | 变更对象内码 |
| 8 | fcreatedatefield | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fchangeobjname | 变更对象名称 | varchar | 255 |  | √ | ' ' | 变更对象名称 |
| 11 | fchangeobjmodel | 变更业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 12 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fchangeobjversionid | 版本id | varchar | 50 |  | √ | ' ' | 版本id |
| 15 | fchangeobjversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |
| 16 | fchangeobjrelatebill | 关联变更单 | varchar | 50 |  | √ | ' ' | 关联变更单 |
| 17 | fchangeobjnumber | 变更对象编码 | varchar | 50 |  | √ | ' ' | 变更对象编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rm_changeobj_m0 |  | fchangeobjtempid |
| 2 | pk_plm_rm_changeobj |  | fid |

---

## 变更对象-多语言表 t_plm_rm_changeobj_l

- **表名称：** 变更对象-多语言表
- **表名：** t_plm_rm_changeobj_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fchangeobjname | 变更对象名称 | varchar | 399 |  | √ | ' ' | 变更对象名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rm_changeobj_l_0 |  | fid,flocaleid |
| 2 | pk_plm_rm_changeobj_l |  | fpkid |

---

## 影响项目-多选基础资料表 t_plm_rm_chagneobj_prj

- **表名称：** 影响项目-多选基础资料表
- **表名：** t_plm_rm_chagneobj_prj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [影响项目 plm_rm_effectprj](../plmrm_files/plm_rm_effectprj.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rm_chagneobj_prj_fk |  | fid |
| 2 | pk_plm_rm_chagneobj_prj |  | fpkid |

---

## 影响对象-多选基础资料表 t_plm_rm_chagneobj_obj

- **表名称：** 影响对象-多选基础资料表
- **表名：** t_plm_rm_chagneobj_obj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [影响对象 plm_rm_effectobj](../plmrm_files/plm_rm_effectobj.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rm_chagneobj_obj_fk |  | fid |
| 2 | pk_plm_rm_chagneobj_obj |  | fpkid |

---

## 变更对象负责人-多选基础资料表 t_plm_rm_changeobj_per

- **表名称：** 变更对象负责人-多选基础资料表
- **表名：** t_plm_rm_changeobj_per

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rm_changeobj_per_fk |  | fid |
| 2 | pk_plm_rm_changeobj_per |  | fpkid |

---

## 影响预算-多选基础资料表 t_plm_rm_chagneobj_pb

- **表名称：** 影响预算-多选基础资料表
- **表名：** t_plm_rm_chagneobj_pb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [影响预算 plm_rm_effectpb](../plmrm_files/plm_rm_effectpb.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rm_chagneobj_pb_fk |  | fid |
| 2 | pk_plm_rm_chagneobj_pb |  | fpkid |
