# 权限日志业务类型-permlog_busitype

## 权限日志业务类型-多语言表 t_permlog_busitype_l

- **表名称：** 权限日志业务类型-多语言表
- **表名：** t_permlog_busitype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbusitype_desc | 业务类型描述 | varchar | 255 |  | √ | ' ' | 业务类型描述 |
| 3 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_permlog_busitype_l |  | fid,flocaleid |
| 2 | pk_t_permlog_busitype_l |  | fpkid |

---

## 权限日志业务类型-主表 t_permlog_busitype

- **表名称：** 权限日志业务类型-主表
- **表名：** t_permlog_busitype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbusitype | 业务类型 | varchar | 255 |  | √ | ' ' | 业务类型 |
| 4 | fdirect_savediff | 是否直接保存差异 | bpchar | 1 |  | √ | '0' | 是否直接保存差异 |
| 5 | fvisible | 可见性 | bpchar | 1 |  | √ | '1' | 可见性,枚举: 0 :隐藏 1 :可见 |
| 6 | farchivea_retaindays | 归档保留时长 | int4 | 32 |  | √ | 0 | 归档保留时长 |
| 7 | fbusitype_desc | 业务类型描述 | varchar | 255 |  | √ | ' ' | 业务类型描述 |
| 8 | fmodify_time | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 9 | farchivea_period | 日志归档周期 | int4 | 32 |  | √ | 0 | 日志归档周期 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 12 | fdetail_form | 详情表单页面 | varchar | 255 |  | √ | ' ' | 详情表单页面 |
| 13 | fdiff_handler | 日志差异处理类 | varchar | 255 |  | √ | ' ' | 日志差异处理类 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_permlog_busitype |  | fbusitype |
| 2 | pk_t_permlog_busitype |  | fid |
