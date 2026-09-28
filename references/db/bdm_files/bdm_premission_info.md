# 发票许可信息-bdm_premission_info

## 发票许可信息-主表 t_bdm_premission_info

- **表名称：** 发票许可信息-主表
- **表名：** t_bdm_premission_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fimcappid | 发票云appid | varchar | 50 |  | √ | ' ' | 发票云appid |
| 3 | fimcsecret | 发票云secret | varchar | 50 |  | √ | ' ' | 发票云secret |
| 4 | frequesturl | 发票云url | varchar | 200 |  | √ | ' ' | 发票云url |
| 5 | fvalidstatus | 有效状态 | varchar | 30 |  | √ | ' ' | 有效状态,枚举: 0 :有效 1 :失效 |
| 6 | fimscsecret | 税控系统云secret | varchar | 50 |  | √ | ' ' | 税控系统云secret |
| 7 | ffileurl | 许可文件地址 | varchar | 200 |  | √ | ' ' | 许可文件地址 |
| 8 | ftextfield | 税控系统云appid | varchar | 50 |  | √ | ' ' | 税控系统云appid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdm_premission_info |  | fid |
| 2 | idx_bdm_premission_info_id |  | fimcappid |
