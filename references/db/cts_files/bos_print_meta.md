# 打印元数据-bos_print_meta

## 打印元数据-主表 t_svc_printmeta

- **表名称：** 打印元数据-主表
- **表名：** t_svc_printmeta

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fname | 模板名称 | varchar | 256 |  | √ | ' ' | 模板名称 |
| 3 | fbillformid | 实体 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fmodify_v | 更新版本 | int8 | 64 |  | √ | 0 | 更新版本 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 7 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fisv | 开发商标识 | varchar | 50 |  |  | ' ' | 开发商标识 |
| 9 | fstplid | 系统模板ID | varchar | 36 |  | √ | ' ' | 系统模板ID |
| 10 | fbizappid | 应用ID | varchar | 36 |  | √ | ' ' | 应用ID |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fmasterid | 主数据内码 | varchar | 36 |  | √ | ' ' | 主数据内码 |
| 14 | ftype | 模板来源 | bpchar | 1 |  | √ | ' ' | 模板来源,枚举: A :旧模板 B :新模板 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | ftpltype | 模版类型 | bpchar | 1 |  | √ | '0' | 模版类型,枚举: 0 :业务模版 1 :系统模版 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 模板编码 | varchar | 80 |  | √ | ' ' | 模板编码 |
| 19 | fdata | fdata | text | 0 |  |  | null |  |
| 20 | fversion | 版本 | varchar | 30 |  | √ | ' ' | 版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_svc_printmeta |  | fid |
| 2 | idx_svc_printmeta_n |  | fnumber |

---

## 打印元数据-多语言表 t_svc_printmeta_l

- **表名称：** 打印元数据-多语言表
- **表名：** t_svc_printmeta_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fname | 模板名称 | varchar | 256 |  | √ | ' ' | 模板名称 |
| 3 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 4 | fdata | fdata | text | 0 |  |  | null |  |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_svc_printmeta_l |  | fpkid |
| 2 | idx_svc_printmeta_l |  | fid,flocaleid |
