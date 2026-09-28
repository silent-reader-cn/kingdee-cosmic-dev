# 自定义模板-cvp_template

## 自定义模板-多语言表 t_cvp_template_l

- **表名称：** 自定义模板-多语言表
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
| 1 | pk_t_cvp_template_l |  | fpkid |
| 2 | idx_cvp_template_l |  | fid,flocaleid |

---

## 自定义模板-主表 t_cvp_template

- **表名称：** 自定义模板-主表
- **表名：** t_cvp_template

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | ftemptablehead | 模板识别表头信息 | text | 0 |  |  | ' ' | 模板识别表头信息 |
| 4 | fbindingid | 绑定数据ID | int8 | 64 |  | √ | 0 | 绑定数据ID |
| 5 | ftestimgpath | 测试图片 | varchar | 1000 |  | √ | ' ' | 测试图片 |
| 6 | fbindingdata | 绑定数据 | bpchar | 1 |  | √ | '0' | 绑定数据,枚举: 0 :未绑定 1 :绑定 |
| 7 | ftemprenfenceinfo | 模板参照字段信息(锚点信息+控件信息)) | text | 0 |  |  | ' ' | 模板参照字段信息(锚点信息+控件信息)) |
| 8 | fdescription | 模板说明 | varchar | 255 |  | √ | ' ' | 模板说明 |
| 9 | falgoid | 算法ID | varchar | 255 |  | √ | ' ' | 算法ID |
| 10 | ftempimg | 模板原图 | varchar | 1000 |  | √ | ' ' | 模板原图 |
| 11 | fstatus | 模板状态 | bpchar | 1 |  | √ | 'A' | 模板状态,枚举: A :未发布 B :可用 C :禁用 D :已发布-有更新 |
| 12 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fnumber | 模板编码 | varchar | 255 |  | √ | ' ' | 模板编码 |
| 16 | fisvalid | 是否预置 | bpchar | 1 |  | √ | '1' | 是否预置,枚举: 0 :自定义 1 :预置-已发布识别服务 2 :预置-OCR自定义模板 |
| 17 | ftemplatemap | 模板解析映射 | varchar | 1000 |  | √ | ' ' | 模板解析映射 |
| 18 | freferenceimg | 旋转后模板图片 | varchar | 1000 |  | √ | ' ' | 旋转后模板图片 |
| 19 | ftemptageinfo | 模板识别标注信息 | text | 0 |  |  | ' ' | 模板识别标注信息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cvp_template |  | fbindingdata,fstatus,fnumber,fid |
| 2 | pk_t_cvp_template |  | fid |
