# 自定义模板识别关联设置-cvp_plan

## 模板名称-多选基础资料表 t_cvp_plan_template

- **表名称：** 模板名称-多选基础资料表
- **表名：** t_cvp_plan_template

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [模板基础资料 cvp_template_base](../cvp_files/cvp_template_base.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cvp_plan_template |  | fpkid |
| 2 | idx_cvp_plan_template |  | fbasedataid |

---

## 自定义模板识别关联设置-主表 t_cvp_plan

- **表名称：** 自定义模板识别关联设置-主表
- **表名：** t_cvp_plan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fuseclassifier | 是否使用组合识别器 | bpchar | 1 |  |  | '0' | 是否使用组合识别器 |
| 6 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | ftemplatenumber | 模板数 | int8 | 64 |  | √ | 0 | 模板数 |
| 8 | fbusinessobject | 业务对象 | varchar | 255 |  |  | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 9 | ftemplateconfig | 模板配置 | text | 0 |  |  | ' ' | 模板配置 |
| 10 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 11 | fdescription | 说明 | varchar | 255 |  |  | ' ' | 说明 |
| 12 | fclassifier | 组合识别器 | int8 | 64 |  | √ | 0 | [文档分类 cvp_cls_info](../cvp_files/cvp_cls_info.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cvp_plan |  | fnumber,fbusinessobject,fcreatorid |
| 2 | pk_t_cvp_plan |  | fid |
