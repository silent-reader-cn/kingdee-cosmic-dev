# 结账计划-gl_closeplan

## 结账计划-主表 t_gl_closeplan

- **表名称：** 结账计划-主表
- **表名：** t_gl_closeplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 3 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 4 | fplanbiz | 计划模块 | varchar | 30 |  | √ | ' ' | 计划模块 |
| 5 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 6 | fstartdate | 版本化日期 | timestamp | 0 |  |  | null | 版本化日期 |
| 7 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fday | 天数 | int4 | 32 |  | √ | 0 | 天数 |
| 10 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gl_closeplan |  | fid |
| 2 | idx_closeplan_orgid |  | forgid |
