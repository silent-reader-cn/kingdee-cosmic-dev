# 批量修改对象配置-xkcts_bm_bizobjsetting

## 批量修改对象配置-多语言表 t_xkcts_bm_bizobjsetting_l

- **表名称：** 批量修改对象配置-多语言表
- **表名：** t_xkcts_bm_bizobjsetting_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdesc | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkcts_bm_bizobjsetting_l |  | fpkid |
| 2 | idx_xkcts_bm_bizobjsetting_l |  | fid,flocaleid |

---

## 批量修改对象配置-主表 t_xkcts_bm_bizobjsetting

- **表名称：** 批量修改对象配置-主表
- **表名：** t_xkcts_bm_bizobjsetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fparentid | 上级id | int8 | 64 |  | √ | 0 | 上级id |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fisv | 开发商标识 | varchar | 50 |  | √ | ' ' | 开发商标识 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fbizappid | 所属应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fbizobjectid | 业务对象编码 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: 0 :系统预置 1 :扩展 2 :自定义 |
| 14 | fenable | 可用状态 | bpchar | 1 |  | √ | '0' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 16 | fdesc | 备注 | varchar | 100 |  | √ | ' ' | 备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkcts_bm_bizobjset_obj |  | fbizobjectid,fisv |
| 2 | pk_t_xkcts_bm_bizobjsetting |  | fid |

---

## 字段配置-子表 t_xkcts_bm_fieldsetting

- **表名称：** 字段配置-子表
- **表名：** t_xkcts_bm_fieldsetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fieldcondition | 允许批改条件 | varchar | 255 |  | √ | ' ' | 允许批改条件 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | ffieldconditiontype | 允许批改条件类型 | varchar | 50 |  | √ | ' ' | 允许批改条件类型,枚举: 1 :自定义 2 :插件 |
| 5 | ffieldnumber | 字段编码 | varchar | 50 |  | √ | ' ' | 字段编码 |
| 6 | fisdisplay | 是否显示 | bpchar | 1 |  | √ | '1' | 是否显示 |
| 7 | fisallow | 允许批改 | bpchar | 1 |  | √ | '0' | 允许批改 |
| 8 | fislock | 是否锁定 | bpchar | 1 |  | √ | '0' | 是否锁定 |
| 9 | ffielddesc | 描述说明 | varchar | 100 |  | √ | ' ' | 描述说明 |
| 10 | fisfield | 是否字段 | bpchar | 1 |  | √ | '0' | 是否字段 |
| 11 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 12 | fieldcondition_tag | 允许批改条件_详情 | text | 0 |  |  | null | 允许批改条件_详情 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkcts_bm_fieldsetting |  | fentryid |
| 2 | idx_xkcts_bm_fieldsetting_fk |  | fid |

---

## 树形单据体-子表 t_xkcts_bm_fieldgroup

- **表名称：** 树形单据体-子表
- **表名：** t_xkcts_bm_fieldgroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgroupkey | 关联字段key | varchar | 50 |  |  | ' ' | 关联字段key |
| 3 | fgroupplugins_tag | 页面插件_详情 | text | 0 |  |  | null | 页面插件_详情 |
| 4 | fgroupfields | 关联字段 | varchar | 255 |  | √ | ' ' | 关联字段 |
| 5 | fgroupfields_tag | 关联字段_详情 | text | 0 |  |  | null | 关联字段_详情 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 8 | fgroupplugins | 页面插件 | varchar | 255 |  | √ | ' ' | 页面插件 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fgrouplock | 是否锁定 | bpchar | 1 |  | √ | '0' | 是否锁定 |
| 11 | fgroupdesc | 描述说明 | varchar | 100 |  | √ | ' ' | 描述说明 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkcts_bm_fieldgroup |  | fentryid |
| 2 | idx_xkcts_bm_fieldgroup_fk |  | fid |
