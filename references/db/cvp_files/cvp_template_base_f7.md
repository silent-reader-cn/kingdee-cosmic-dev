# 模版基础资料F7-cvp_template_base_f7

## 模版基础资料F7-多语言表 t_cvp_template_l

- **表名称：** 模版基础资料F7-多语言表
- **表名：** t_cvp_template_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 模板名称 | varchar | 50 |  | √ | ' ' | 模板名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | '0' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cvp_template_l |  | fid,flocaleid |
| 2 | pk_t_cvp_template_l |  | fpkid |

---

## 模版基础资料F7-主表 t_cvp_template

- **表名称：** 模版基础资料F7-主表
- **表名：** t_cvp_template

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | ftemptablehead | ftemptablehead | text | 0 |  |  | ' ' |  |
| 4 | fbindingid | 绑定数据ID | int8 | 64 |  | √ | 0 | 绑定数据ID |
| 5 | ftestimgpath | ftestimgpath | varchar | 1000 |  | √ | ' ' |  |
| 6 | fbindingdata | 绑定数据 | bpchar | 1 |  | √ | '0' | 绑定数据,枚举: 0 :未绑定 1 :绑定 |
| 7 | ftemprenfenceinfo | ftemprenfenceinfo | text | 0 |  |  | ' ' |  |
| 8 | fdescription | 模板说明 | varchar | 255 |  | √ | ' ' | 模板说明 |
| 9 | falgoid | falgoid | varchar | 255 |  | √ | ' ' |  |
| 10 | ftempimg | ftempimg | varchar | 1000 |  | √ | ' ' |  |
| 11 | fstatus | 模板状态 | bpchar | 1 |  | √ | 'A' | 模板状态,枚举: A :未发布 B :可用 C :禁用 D :已发布-有更新 |
| 12 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fnumber | 模板编码 | varchar | 255 |  | √ | ' ' | 模板编码 |
| 16 | fisvalid | 是否预置 | bpchar | 1 |  | √ | '1' | 是否预置,枚举: 0 :自定义 1 :预置-已发布识别服务 2 :预置-OCR自定义模板 |
| 17 | ftemplatemap | ftemplatemap | varchar | 1000 |  | √ | ' ' |  |
| 18 | freferenceimg | freferenceimg | varchar | 1000 |  | √ | ' ' |  |
| 19 | ftemptageinfo | ftemptageinfo | text | 0 |  |  | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cvp_template |  | fbindingdata,fstatus,fnumber,fid |
| 2 | pk_t_cvp_template |  | fid |
