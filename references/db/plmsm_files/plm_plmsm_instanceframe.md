# PDM数据实例框架页-plm_plmsm_instanceframe

## PDM数据实例框架页-多语言表 t_plmsm_instancepage_l

- **表名称：** PDM数据实例框架页-多语言表
- **表名：** t_plmsm_instancepage_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmsm_instancepage_l |  | fpkid |
| 2 | idx_plmsm_instancepage_l_0 |  | fname |

---

## 打开单据参数-子表 t_plmsm_instancepage_para

- **表名称：** 打开单据参数-子表
- **表名：** t_plmsm_instancepage_para

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparamvalue | 参数值 | varchar | 50 |  | √ | ' ' | 参数值 |
| 3 | fparamname | 参数名 | varchar | 50 |  | √ | ' ' | 参数名 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmsm_instancepage_para |  | fentryid |
| 2 | idx_plmsm_instancepage_para |  | fid |

---

## PDM数据实例框架页-主表 t_plmsm_instancepage

- **表名称：** PDM数据实例框架页-主表
- **表名：** t_plmsm_instancepage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fsequence | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 4 | fbillstatus | 打开单据状态 | varchar | 50 |  | √ | ' ' | 打开单据状态,枚举: 1 :编辑维护 2 :查看 |
| 5 | fformnumber | 单据编码 | varchar | 50 |  | √ | ' ' | 单据编码 |
| 6 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 7 | fisv | 开发者 | varchar | 50 |  | √ | ' ' | 开发者 |
| 8 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 9 | fshowtype | 打开方式 | varchar | 50 |  | √ | ' ' | 打开方式,枚举: 1 :单据 2 :列表 3 :动态表单 4 :报表 |
| 10 | fispreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmsm_instancepage |  | fid |
| 2 | idx_plmsm_instancepage_no |  | fnumber |
