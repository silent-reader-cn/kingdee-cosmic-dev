# 注册的可搜索文本-bd_regtextinfo

## 注册的可搜索文本-主表 t_bd_regtextinfo

- **表名称：** 注册的可搜索文本-主表
- **表名：** t_bd_regtextinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 注册状态 | bpchar | 1 |  | √ | '3' | 注册状态,枚举: 0 :新增 3 :启用 9 :删除 |
| 3 | fregtext | 注册文本内容 | varchar | 255 |  | √ | ' ' | 注册文本内容 |
| 4 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 期间 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 7 | frefcount | 引用计数 | int4 | 32 |  | √ | 0 | 引用计数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_regtextinfo |  | fid |
| 2 | idx_bd_regtextinfo_un_1 |  | fregtext,forgid,fperiodid,fstatus |

---

## 源记录与注册文本关联关系-子表 t_bd_regtextownership

- **表名称：** 源记录与注册文本关联关系-子表
- **表名：** t_bd_regtextownership

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fownerrecid | 目标主记录ID | int8 | 64 |  | √ | 0 | 目标主记录ID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_regtextownership_1 |  | fid |
| 2 | pk_bd_regtextownership |  | fentryid |
