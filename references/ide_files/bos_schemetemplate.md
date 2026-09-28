# 方案模板-bos_schemetemplate

## 方案模板-主表 t_bas_programtemplate

- **表名称：** 方案模板-主表
- **表名：** t_bas_programtemplate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | 方案模板分组 bos_schemegroup |
| 4 | fjson | json存储 | varchar | 256 |  | √ | ' ' | json存储 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | ftitle | 控件方案组名 | varchar | 100 |  | √ | ' ' | 控件方案组名 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fvalue | 分类 | int4 | 32 |  | √ | 0 | 分类 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fmulcolums | 多行纵列 | bpchar | 1 |  | √ | '0' | 多行纵列 |
| 13 | forder | 顺序 | int4 | 32 |  | √ | 0 | 顺序 |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 16 | fjson_tag | json存储_详情 | text | 0 |  |  | null | json存储_详情 |
| 17 | fimage | 缩略图 | varchar | 256 |  | √ | ' ' | 缩略图 |
| 18 | fsmallimg | 小图显示 | bpchar | 1 |  | √ | '0' | 小图显示 |
| 19 | fhoverimg | 悬停图 | varchar | 256 |  | √ | ' ' | 悬停图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_programtemplate |  | fid |
| 2 | idx_bas_programtemplate_number |  | fnumber |

---

## 方案模板-多语言表 t_bas_programtemplate_l

- **表名称：** 方案模板-多语言表
- **表名：** t_bas_programtemplate_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftitle | ftitle | varchar | 100 |  | √ | ' ' |  |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_programtemplate_l_id |  | fid,flocaleid |
| 2 | pk_t_bas_programtemplate_l |  | fpkid |
