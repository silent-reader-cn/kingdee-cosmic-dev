# 预算首页设置-xkbm_homepagerasetting

## 预算首页设置-主表 t_xkbm_homepagerasetting

- **表名称：** 预算首页设置-主表
- **表名：** t_xkbm_homepagerasetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxkbmbusinessservice | 预算业务服务 | int8 | 64 |  | √ | 0 | 预算业务服务 xkbm_businessservice |
| 3 | fdays | 天数 | int4 | 32 |  | √ | 0 | 天数 |
| 4 | fcalculatesource | 统计依据 | varchar | 30 |  | √ | ' ' | 统计依据,枚举: 1 :统一默认截止日 2 :根据预算方案设置截止日 |
| 5 | funifiedtype | 统一截止日类型 | varchar | 30 |  | √ | ' ' | 统一截止日类型,枚举: 1 :当期开始前 2 :上期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_homepage_ra_set |  | fxkbmbusinessservice |
| 2 | pk_xkbm_homepagerasetting |  | fid |
