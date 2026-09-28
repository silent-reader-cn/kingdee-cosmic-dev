# 报表模板项目关系-xkrpt_iteminsample

## 单据体-子表 t_xkrpt_iteminsampleentry

- **表名称：** 单据体-子表
- **表名：** t_xkrpt_iteminsampleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fitemdatatypeid | 项目数据类型编码 | int8 | 64 |  | √ | 0 | 项目数据类型 xkbd_rptitemdatatype |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | frptitemid | 报表项目编码 | int8 | 64 |  | √ | 0 | 报表项目 xkbd_rptitem |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkrpt_iteminsampleentry |  | fentryid |
| 2 | idx_xkrpt_iteminsampleery_fid |  | fid |

---

## 报表模板项目关系-主表 t_xkrpt_iteminsample

- **表名称：** 报表模板项目关系-主表
- **表名：** t_xkrpt_iteminsample

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frptid | 报表模板编码 | varchar | 36 |  | √ | ' ' | 报表模板 xkrpt_rptsample |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkrpt_iteminsample |  | fid |
| 2 | idx_xkrpt_iteminsample_frptid |  | frptid |
