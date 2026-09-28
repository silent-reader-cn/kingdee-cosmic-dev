# 通用扩展点注册-bos_genextcase

## 通用扩展点注册-主表 t_meta_genextcase

- **表名称：** 通用扩展点注册-主表
- **表名：** t_meta_genextcase

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcase_type | 分类 | varchar | 30 |  | √ | ' ' | 分类,枚举: op :操作 |
| 3 | flifeevent | 绑定事件 | varchar | 100 |  |  | null | 绑定事件 |
| 4 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 7 | fdef_open | 默认开放 | bpchar | 1 |  | √ | '0' | 默认开放 |
| 8 | fisv | 开发商 | varchar | 100 |  | √ | ' ' | 开发商 |
| 9 | finterface | 扩展点接口 | varchar | 200 |  | √ | ' ' | 扩展点接口 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | ftemplate_tag | 脚本模板_详情 | text | 0 |  |  | null | 脚本模板_详情 |
| 15 | fenable | 使用状态 | bpchar | 50 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 17 | fdesc | 扩展说明 | varchar | 200 |  |  | null | 扩展说明 |
| 18 | fversion | 生效版本 | varchar | 50 |  | √ | ' ' | 生效版本 |
| 19 | fdesc_tag | 扩展说明_详情 | text | 0 |  |  | null | 扩展说明_详情 |
| 20 | ftemplate | 脚本模板 | varchar | 200 |  |  | null | 脚本模板 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_meta_genextcase |  | fid |
| 2 | idx_meta_genextca_number |  | fnumber |

---

## 通用扩展点注册-多语言表 t_meta_genextcase_l

- **表名称：** 通用扩展点注册-多语言表
- **表名：** t_meta_genextcase_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_meta_genextcase_l_id |  | fid,flocaleid |
| 2 | pk_meta_genextcase_l |  | fpkid |
