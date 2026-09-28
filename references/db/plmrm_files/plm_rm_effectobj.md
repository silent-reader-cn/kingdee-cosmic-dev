# 影响对象-plm_rm_effectobj

## 影响对象-主表 t_plm_rm_effectobj

- **表名称：** 影响对象-主表
- **表名：** t_plm_rm_effectobj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | feffectobjversionid | 版本id | varchar | 50 |  | √ | ' ' | 版本id |
| 3 | feffectobjversionlock | 临时版本 | varchar | 50 |  | √ | ' ' | 临时版本 |
| 4 | fcreatedatefield | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | feffectobjrelatebill | 关联变更单 | varchar | 50 |  | √ | ' ' | 关联变更单 |
| 6 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | feffectobjmodel | 影响业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 9 | feffectobjtype | 影响类型 | varchar | 50 |  | √ | ' ' | 影响类型,枚举: parentcontext :上文 childcontext :下文 relation :关联项 |
| 10 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | feffectobjmaster | 影响对象内码 | int8 | 64 |  | √ | 0 | 影响对象内码 |
| 13 | feffectobjbasedataid | 影响对象基础资料 | varchar | 50 |  | √ | ' ' | 影响对象基础资料 |
| 14 | feffectobjoption11 | feffectobjoption11 | varchar | 50 |  | √ | ' ' |  |
| 15 | feffectobjnumber | 影响对象编码 | varchar | 50 |  | √ | ' ' | 影响对象编码 |
| 16 | feffectobjisfinish | 是否完成 | varchar | 50 |  | √ | ' ' | 是否完成,枚举: unfinished :未完成 complete :已完成 |
| 17 | feffectobjtempid | 影响对象临时版本id | varchar | 50 |  | √ | ' ' | 影响对象临时版本id |
| 18 | fchangeobjversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |
| 19 | feffectobj | 影响对象 | int8 | 64 |  | √ | 0 | 影响对象 |
| 20 | feffectobjoption | 变更操作 | int8 | 64 |  | √ | 0 | [影响对象变更操作 plm_rm_change_effectopt](../plmrm_files/plm_rm_change_effectopt.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_rm_effectobj |  | fid |
| 2 | idx_plm_rm_effectobj_m0 |  | feffectobjoption |

---

## 影响对象负责人-多选基础资料表 t_plm_rm_effectobj_per

- **表名称：** 影响对象负责人-多选基础资料表
- **表名：** t_plm_rm_effectobj_per

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
| 1 | pk_plm_rm_effectobj_per |  | fpkid |
| 2 | idx_plm_rm_effectobj_per_fk |  | fid |
